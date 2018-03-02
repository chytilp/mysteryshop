from datetime import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _l
from django.utils import timezone

from model_utils import Choices

from project.models import Project, Wave


class MessageContext(models.Model):

    project = models.ForeignKey(Project, verbose_name=_l('project'), null=True, blank=True,
                                related_name='message_contexts')
    wave = models.ForeignKey(Wave, verbose_name=_l('wave'), null=True, blank=True, related_name='message_contexts')
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    author = models.ForeignKey(User, verbose_name=_l('author'), null=False, blank=False,
                               related_name='message_contexts')


class Message(models.Model):

    STATUS = Choices(
        (1, 'NEW', _l('New')),
        (2, 'ASSIGN', _l('Assign')),
        (3, 'IN_PROGRESS', _l('In progress')),
        (4, 'SOLVED', _l('Solved')),
        (5, 'UNSOLVABLE', _l('Unsolvable'))
    )

    context = models.ForeignKey(MessageContext, verbose_name=_l('message context'), null=True, blank=True,
                                related_name='messages')
    from_user = models.ForeignKey(User, verbose_name=_l('from user'), null=False, blank=False,
                                  related_name='from_messages')
    to_user = models.ForeignKey(User, verbose_name=_l('to user'), null=False, blank=False, related_name='to_messages')
    content = models.TextField(verbose_name=_l('content'), null=False, blank=False)
    title = models.CharField(verbose_name=_l('title'), max_length=100, null=False, blank=False)
    sent_when = models.DateTimeField(verbose_name=_l('sent when'), null=True, blank=True, editable=False)
    solver = models.ForeignKey(User, verbose_name=_l('solver'), null=True, blank=True, related_name='solver_messages')
    status = models.PositiveIntegerField(verbose_name=_l('status'), choices=STATUS, default=STATUS.NEW)
    current_status_from = models.DateTimeField(verbose_name=_l('current status from'), null=True, blank=True,
                                               default=timezone.now)
    related_communication_id = models.PositiveIntegerField(verbose_name=_l('related communication id'), null=True,
                                                           blank=True)

    def __str__(self):
        return '{} -> {}: {}'.format(self.from_user.get_full_name(), self.to_user.get_full_name(), self.title)
