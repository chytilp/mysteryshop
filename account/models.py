from enum import IntEnum

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _l

from model_utils import Choices

from utils.fields import PhoneNumberField


class Candidate(models.Model):

    STATUS = Choices(
        (1, 'NEW', _l('New')),
        (2, 'IN_PROGRESS', _l('In progress')),
        (3, 'APPROVED', _l('Approved')),
    )

    EDUCATION = Choices(
        (1, 'BASIC', _l('Basic')),
        (2, 'SECONDARY', _l('Secondary')),
        (3, 'SECONDARY_GRADUATED', _l('Secondary graduated')),
        (4, 'COLLEGE', _l('College')),
    )

    first_name = models.CharField(verbose_name=_l('first name'), null=False, blank=False, max_length=50)
    last_name = models.CharField(verbose_name=_l('last name'), null=False, blank=False, max_length=50)
    email = models.EmailField(verbose_name=_l('first name'), null=False, blank=False)
    personal_id = models.CharField()  # TODO: dodelat
    phone = PhoneNumberField(verbose_name=_l('phone'), blank=False, null=False)
    is_man = models.BooleanField(verbose_name=_l('is man'), blank=False, null=False)
    districts = models.TextField(verbose_name=_l('working districts'), blank=False, null=False)
    city = models.CharField(verbose_name=_l('city'), blank=False, null=False)
    address = models.CharField(verbose_name=_l('address'), blank=False, null=False)
    zip_code = models.PositiveSmallIntegerField(verbose_name=_l('zip code'))
    status = models.PositiveIntegerField(verbose_name=_l('status'), choices=STATUS, default=STATUS.NEW, blank=False,
                                         null=False)
    education = models.PositiveIntegerField(verbose_name=_l('education'), choices=EDUCATION, blank=False, null=False)
    registered = models.DateTimeField(verbose_name=_l('registered'), auto_created_now=True)
    status_change_by = models.ForeignKey(User, verbose_name=_l('status was changed by'), blank=True, null=True,
                                         related_name='candidates')
    status_change_when = models.DateTimeField(verbose_name=_l('status was changed when'), blank=True, null=True)
    cancel_reason = models.TextField(verbose_name=_l('reason of cancellation'), blank=True, null=True)


class Interviewer(models.Model):

    user = models.OneToOneField(User, verbose_name=_l('app user'), blank=False, null=False, related_name='interviewer')
    phone = PhoneNumberField(verbose_name=_l('phone'), blank=True, null=True)
    bank_account = models.CharField(verbose_name=_l('bank account'), blank=True, null=True, max_length=30)  # TODO: dodelat
    visit_districts = models.ManyToManyField('project.District', verbose_name=_l('working districts'),
                                             through='InterviewerDistrict')

    def __str__(self):
        return 'interviewer ' + self.user.get_full_name()


class InterviewerDistrict(models.Model):

    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'),  null=False, blank=False,
                                    related_name='districts')
    district = models.ForeignKey('project.District', verbose_name=_l('district'), null=False, blank=False,
                                 related_name='interviewers')
    is_home = models.BooleanField(verbose_name=_l('is home district'), default=False)

    def __str__(self):
        return self.interviewer.user.get_full_name() + ' (' + self.district.slug + ')'


class InterviewerStatus(models.Model):

    STATUS = Choices(
        (1, 'UNAPPROVED', _l('Unapproved')),
        (2, 'CANCELLED', _l('Cancelled')),
        (3, 'ACTIVE', _l('Active')),
        (4, 'PAUSED', _l('Paused')),
        (5, 'FINISHED', _l('Finished'))
    )

    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), null=False, blank=False, related_name='statuses')
    status = models.PositiveIntegerField(verbose_name=_l('status'), choices=STATUS, default=STATUS.UNAPPROVED)
    begin = models.DateTimeField(verbose_name=_l('begin date'), null=False, blank=False)

    def __str__(self):
        return '{}-{}-{}'.format(self.interviewer.user.get_full_name(), self.status, self.begin)
