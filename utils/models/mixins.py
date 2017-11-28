from django.db import models


class ActiveFieldMixin(models.Model):

    active = models.DateField(blank=True, null=True, default=None)

    @property
    def is_active(self):
        return True if not self.active else False

    @property
    def when_rejected(self):
        return '' if not self.active else str(self.active)

    class Meta:
        abstract = True


class SimpleEnumClassMixin:

    def __str__(self):
        return '{} ({})'.format(self.name, self.__class__.__name__)