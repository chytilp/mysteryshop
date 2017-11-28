from django.db import models
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text

from .strings import normalize_phone_number
from . import forms as utils_forms


class PhoneNumberField(models.CharField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{**kwargs, **{'max_length': 13}})

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs['max_length'] = 14
        kwargs.setdefault('form_class', utils_forms.PhoneNumberField)
        return super(PhoneNumberField, self).formfield(**kwargs)

    def clean(self, value, model_instance):
        try:
            return super().clean(normalize_phone_number(value), model_instance)
        except ValueError as e:
            raise ValidationError(force_text(e))
