import re
from datetime import date

from dateutil.relativedelta import relativedelta

from django.core.exceptions import ValidationError
from django.db.models.fields import CharField

from .validators import BankAccountValidator, CZBirthNumberValidator, IDCardNoValidator, personal_id_date


class CZBirthNumber(str):

    MALE = 'M'
    FEMALE = 'F'

    def age(self, now=None):
        now = now or date.today()
        birth_date = self.date()
        return relativedelta(now, birth_date).years if birth_date else -1

    def is_valid(self):
        try:
            CZBirthNumberValidator()(self)
            return True
        except ValidationError:
            return False

    def date(self):
        try:
            return personal_id_date(self)
        except ValueError:
            return None

    def sex(self):
        return self.FEMALE if int(self[2:4]) > 50 else self.MALE if self else None


class CZBirthNumberDeferredAttribute(object):

    def __init__(self, field_name):
        self.field_name = field_name

    def __set__(self, instance, value):
        instance.__dict__[self.field_name] = CZBirthNumber(value) if value is not None else value


class CZBirthNumberField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super(CharField, self).__init__(*args, **kwargs)
        self.validators.append(CZBirthNumberValidator())

    def contribute_to_class(self, cls, name, virtual_only=False):
        super().contribute_to_class(cls, name, virtual_only=virtual_only)
        setattr(cls, self.attname, CZBirthNumberDeferredAttribute(self.attname))

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        return value.replace('/', '') if value else value


class RawCopyCZBirthNumberField(CZBirthNumberField):

    def __init__(self, *args, **kwargs):
        self.copy_to_field = kwargs.pop('copy_to_field', None)
        kwargs['null'] = True
        kwargs['blank'] = True
        super(RawCopyCZBirthNumberField, self).__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        if self.copy_to_field and hasattr(model_instance, self.copy_to_field):
            setattr(model_instance, self.copy_to_field,
                    model_instance._meta.get_field(self.copy_to_field).clean(value, model_instance))

        value = self.to_python(value)
        try:
            return super().clean(value, model_instance)
        except ValidationError:
            return None


class IDCardNoField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super(CharField, self).__init__(*args, **kwargs)
        self.validators.append(IDCardNoValidator())


def parse_bank_account(whole_bank_account):
    BANK_ACCOUNT_PATTERN = re.compile(r'^((0*(?P<prefix>[1-9]\d*)?)-)?(0*(?P<number>[1-9]\d*))/(?P<bank>\d+)$')
    match = BANK_ACCOUNT_PATTERN.match(whole_bank_account)
    if match:
        return (match.groupdict()['prefix'] or '', match.groupdict()['number'], match.groupdict()['bank'])
    else:
        return (None, None, None)


class BankAccount(object):

    def __init__(self, whole_bank_account):
        self.whole_bank_account = whole_bank_account
        self.bank_account_prefix, self.bank_account_number, self.bank_code = parse_bank_account(
            whole_bank_account or '')

    @property
    def bank_account_without_prefix(self):
        return '/'.join((self.bank_account_number, self.bank_code)) if self.whole_bank_account else None

    @property
    def bank_account_with_prefix(self):
        return ('{}-{}/{}'.format(self.bank_account_prefix, self.bank_account_number, self.bank_code)
                if self.bank_account_prefix else '{}/{}'.format(
                    self.bank_account_number, self.bank_code)) if self.whole_bank_account else None

    @property
    def bank_account_number_with_prefix(self):
        return ('-'.join((self.bank_account_prefix, self.bank_account_number))
                if self.bank_account_prefix else self.bank_account_number) if self.whole_bank_account else None

    class RESTMeta:
        direct_serialization_fields = ('bank_account_number', 'bank_code', 'bank_account_number_with_prefix')


class BankAccountDescriptor(object):

    def __init__(self, field_name):
        self.field_name = field_name

    def __get__(self, instance, cls=None):
        return BankAccount(getattr(instance, self.field_name))


class BankAccountNumber(CharField):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **{**{'max_length':24}, **kwargs})
        self.validators.append(BankAccountValidator())

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        return BankAccountValidator()(value) if value else value

    def contribute_to_class(self, cls, name, virtual_only=False):
        super().contribute_to_class(cls, name, virtual_only=virtual_only)
        setattr(cls, '{}_object'.format(self.attname), BankAccountDescriptor(self.attname))
