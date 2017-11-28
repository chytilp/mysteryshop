from django.db import models
from django.utils import timezone
from project.models import Project, Wave
from account.models import Interviewer
from project.models import Shop


class Training(models.Model):
    project = models.ForeignKey(Project)
    interviewer = models.ForeignKey(Interviewer)
    score = models.SmallIntegerField()
    passed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Training({0},{1}),score={2}".format(str(self.interviewer),
                                                    str(self.project),
                                                    self.score)


class Bonus(models.Model):
    wave = models.ForeignKey(Wave)
    interviewer = models.ForeignKey(Interviewer)
    zobdobi = models.DateField()
    bonus = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    paid = models.DateField(blank=True)

    def __str__(self):
        return "Bonus({0},{1}),bonus={2}".format(str(self.interviewer),
                                                 str(self.wave),
                                                 self.bonus)


class Attachment(models.Model):
    wave = models.ForeignKey(Wave)
    shop = models.ForeignKey(Shop)
    interviewer = models.ForeignKey(Interviewer)
    recorded = models.DateTimeField(default=timezone.now)
    data = models.FileField()
    file_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)

    def __str__(self):
        return "Attachment({0},{1},{2}),file={3}".format(str(self.interviewer),
                                                         str(self.wave),
                                                         str(self.shop),
                                                         self.file_name)


class Wage(models.Model):
    wave = models.ForeignKey(Wave)
    interviewer = models.ForeignKey(Interviewer)
    zobdobi = models.DateField()
    wage = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    paid = models.DateField(blank=True)

    def __str__(self):
        return "Wage({0},{1}),wage={2}".format(str(self.interviewer),
                                               str(self.wave),
                                               self.wage)


class Visit(models.Model):
    wave = models.ForeignKey(Wave)
    shop = models.ForeignKey(Shop)
    interviewer = models.ForeignKey(Interviewer, null=True)
    group = models.PositiveIntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    visit_day = models.DateField(blank=True, null=True)
    is_pm = models.NullBooleanField(blank=True)
    data_ident = models.TextField(blank=True, null=True)
    data_recorded = models.DateTimeField(blank=True, null=True)
    wage = models.ForeignKey(Wage, blank=True, null=True, related_name='visits')

    def __str__(self):
        return "Visit({0},{1},{2}),visit={3},done={4}".format(str(self.interviewer),
                                                              str(self.wave),
                                                              str(self.shop),
                                                              (str(self.visit_day) if self.visit_day else "-"), \
                                                              ("y" if self.data_recorded else "n"))
