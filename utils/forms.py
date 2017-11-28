from django import forms
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text

from .strings import normalize_phone_number


class PhoneNumberField(forms.CharField):

    def clean(self, value):
        try:
            return normalize_phone_number(super().clean(value))
        except ValueError as e:
            raise ValidationError(force_text(e))
