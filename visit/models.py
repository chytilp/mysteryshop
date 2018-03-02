from jsonfield.fields import JSONField

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _l

from project.models import Project, Wave
from account.models import Interviewer
from project.models import Shop


class Test(models.Model):

    project = models.ForeignKey(Project, verbose_name=_l('project'), blank=False, null=False, related_name='tests')
    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), blank=False, null=False,
                                    related_name='tests')
    score = models.PositiveSmallIntegerField(verbose_name=_l('test score'), blank=False, null=False)
    passed = models.DateTimeField(verbose_name=_l('test was passed when'), blank=True, null=True)

    def __str__(self):
        return "Test({0},{1}),score={2}".format(str(self.interviewer), str(self.project), str(self.score))


class Attachment(models.Model):

    wave = models.ForeignKey(Wave, verbose_name=_l('wave'), null=False, blank=False, related_name='attachments')
    shop = models.ForeignKey(Shop, verbose_name=_l('shop'), null=False, blank=False, related_name='attachments')
    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), null=False, blank=False,
                                    related_name='attachments')
    recorded = models.DateTimeField(verbose_name=_l('recorded when'), null=False, blank=False, default=timezone.now,
                                    editable=False)
    data = models.FileField(verbose_name=_l('data file'), null=False, blank=False, upload_to='data')
    file_name = models.CharField(verbose_name=_l('name of data file'), max_length=100, null=False, blank=False)
    type = models.CharField(verbose_name=_l('type of data file'), max_length=10, null=False, blank=False)

    def __str__(self):
        return "Attachment({0},{1},{2}),file={3}".format(str(self.interviewer),
                                                         str(self.wave),
                                                         str(self.shop),
                                                         self.file_name)


class Wage(models.Model):

    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), null=False, blank=False,
                                    related_name='wages')
    billing_period = models.DateField(verbose_name=_l('billing period'), null=False, blank=False)
    amount = models.DecimalField(verbose_name=_l('amount of money'), decimal_places=2, max_digits=7, null=False,
                                 blank=False)
    description = models.TextField(verbose_name=_l('description'), blank=True, null=True)
    requested = models.DateTimeField(verbose_name=_l('description'), blank=False, null=False, default=timezone.now,
                                     editable=False)
    paid = models.BooleanField(verbose_name=_l('wage was paid'), blank=False, null=False, default=False)

    def __str__(self):
        return "Wage({0},{1}),wage={2}".format(str(self.interviewer), str(self.billing_period), str(self.amount))


class Bonus(models.Model):

    wave = models.ForeignKey(Wave, verbose_name=_l('wave'), null=False, blank=False, related_name='bonuses')
    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), null=False, blank=False,
                                    related_name='bonuses')
    wage = models.ForeignKey(Wage, verbose_name=_l('wage'), null=True, blank=True, related_name='bonuses')
    amount = models.DecimalField(verbose_name=_l('amount of money'), decimal_places=2, max_digits=7, null=False,
                                 blank=False)
    description = models.TextField(verbose_name=_l('description'), null=False, blank=False)

    def __str__(self):
        return "Bonus({0},{1}),bonus={2}".format(str(self.interviewer),
                                                 str(self.wave),
                                                 self.amount)


class Visit(models.Model):

    wave = models.ForeignKey(Wave, verbose_name=_l('wave'), null=False, blank=False, related_name='visits')
    shop = models.ForeignKey(Shop, verbose_name=_l('shop'), null=False, blank=False, related_name='visits')
    interviewer = models.ForeignKey(Interviewer, verbose_name=_l('interviewer'), null=True, blank=True,
                                    related_name='visits')
    group = models.PositiveIntegerField(verbose_name=_l('group of shops'), null=False, blank=False)
    date_from = models.DateField(verbose_name=_l('visit from date'), null=False, blank=False)
    date_to = models.DateField(verbose_name=_l('visit to date'), null=False, blank=False)
    visit_day = models.DateField(verbose_name=_l('visit date'), blank=True, null=True)
    is_pm = models.NullBooleanField(verbose_name=_l('is pm time'), blank=True, null=True)
    data = JSONField(verbose_name=_l('questionnaire data'), null=True, blank=True)
    data_recorded = models.DateTimeField(verbose_name=_l('data recorded when'), blank=True, null=True)
    wage = models.ForeignKey(Wage, verbose_name=_l('wage'), blank=True, null=True, related_name='visits')

    def __str__(self):
        return "Visit({0},{1},{2}),visit={3},done={4}".format(str(self.interviewer),
                                                              str(self.wave),
                                                              str(self.shop),
                                                              (str(self.visit_day) if self.visit_day else "-"),
                                                              ("y" if self.data_recorded else "n"))
