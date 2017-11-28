from enum import IntEnum

from django.db import models
from django.contrib.auth.models import User

from utils.fields import PhoneNumberField


class Interviewer(models.Model):

    user = models.OneToOneField(User, blank=False, null=False, related_name='interviewer')
    phone = PhoneNumberField(blank=True, null=True)
    bank_account = models.CharField(blank=True, null=True, max_length=30)
    visit_districts = models.ManyToManyField('project.District', through='InterviewerDistrict')

    def __str__(self):
        return 'interviewer ' + self.user.get_full_name()


class InterviewerDistrict(models.Model):

    interviewer = models.ForeignKey(Interviewer, null=False, blank=False)
    district = models.ForeignKey('project.District', null=False, blank=False)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return self.interviewer.user.get_full_name() + ' (' + self.district.slug + ')'


class InterviewerStatus(models.Model):

    class Status(IntEnum):
        UNAPPROVED = 1
        CANCELLED = 2
        ACTIVE = 3
        PAUSED = 4
        FINISHED = 5

    interviewer = models.ForeignKey(Interviewer, null=False, blank=False, related_name='statuses')
    status = models.PositiveIntegerField(choices=Status, default=Status.UNAPPROVED)
    begin = models.DateField(null=False, blank=False)

    def __str__(self):
        return '{}-{}-{}'.format(self.interviewer.user.get_full_name(), self.status, self.begin)
