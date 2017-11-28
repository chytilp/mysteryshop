from enum import IntEnum

from datetime import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from project.models import Project, Wave


class MessageContext(models.Model):

    project = models.ForeignKey(Project, null=True, blank=True)
    wave = models.ForeignKey(Wave, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    author = models.ForeignKey(User, null=False, blank=False)


class Message(models.Model):

    class Status(IntEnum):
        NEW = 1
        ASSIGN = 2
        IN_PROGRESS = 3
        SOLVED = 4
        UNSOLVABLE = 5

    context = models.ForeignKey(MessageContext, null=True, blank=True)
    from_user = models.ForeignKey(User, null=False, blank=False)
    to_user = models.ForeignKey(User, null=False, blank=False)
    content = models.TextField(null=False, blank=False, verbose_name='')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='')
    sent_when = models.DateTimeField(null=True, blank=True, verbose_name='')
    solver = models.ForeignKey(User, null=True, blank=True, verbose_name='')
    status = models.PositiveIntegerField(choices=Status, default=Status.NEW)
    current_status_from = models.DateTimeField(null=True, blank=True, default=datetime.now())
    related = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return '{} -> {}: {}'.format(self.from_user.get_full_name(), self.to_user.get_full_name(), self.title)
