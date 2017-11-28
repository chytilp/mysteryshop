from enum import IntEnum

from django.db import models
from django.db.models import Q

from utils.models.mixins import ActiveFieldMixin, SimpleEnumClassMixin


class Region(models.Model, SimpleEnumClassMixin):

    name = models.CharField(blank=False, null=False, max_length=20)
    slug = models.SlugField(blank=False, null=False, max_length=5)


class District(models.Model, SimpleEnumClassMixin):

    name = models.CharField(blank=False, null=False, max_length=20)
    region = models.ForeignKey(Region, blank=False, null=False, related_name='districts')
    slug = models.SlugField(blank=False, null=False, max_length=10)


class Client(models.Model, SimpleEnumClassMixin):

    name = models.CharField(blank=False, null=False, max_length=50)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=False, null=False, max_length=20)

    @property
    def active_projects(self):
        return self.projects.filter(active__isnull=True)


class ClientCategory(models.Model):

    name = models.CharField(blank=False, null=False, max_length=50)
    client = models.ForeignKey(Client, blank=False, null=False, related_name='categories')
    active = models.BooleanField(blank=False, null=False, default=True)
    sub_category = models.CharField(blank=False, null=False, max_length=20, default='unknown')


class Project(ActiveFieldMixin, SimpleEnumClassMixin):

    name = models.CharField(blank=False, null=False, max_length=50)
    number = models.PositiveIntegerField(blank=False, null=False)
    client = models.ForeignKey(Client, blank=False, null=False, related_name='projects')
    date_from = models.DateField(blank=False, null=False)
    date_to = models.DateField(blank=True, null=True)
    test_cluster = models.PositiveIntegerField(blank=True, null=True)

    @property
    def not_closed_waves(self):
        return self.waves.filter(Q(status=Wave.PREPARING) | Q(status=Wave.ACTIVE) | Q(status=Wave.FINISHED))


class Wave(models.Model):

    class Status(IntEnum):
        PREPARING = 1   #can see admin, interviewer not yet
        ACTIVE = 2      #interviewer can see it
        FINISHED = 3    #lock for interviewer changes
        CLOSED = 4      #move to archive

    number = models.PositiveIntegerField(blank=False, null=False)
    project = models.ForeignKey(Project, blank=False, null=False, related_name='waves')
    date_from = models.DateField(blank=False, null=False)
    date_to = models.DateField(blank=False, null=False)
    status = models.PositiveIntegerField(choices=Status, default=Status.PREPARING)
    fee_full = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fee_part = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_delay_for_full_fee = models.PositiveIntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return 'Project: {}, wave: {}'.format(self.project.name, str(self.number))


class Shop(ActiveFieldMixin):

    name = models.CharField(blank=False, null=False, max_length=50)
    client_code = models.CharField(blank=False, null=False, max_length=10, default='')
    client = models.ForeignKey(Client, blank=False, null=False, related_name='shops')
    district = models.ForeignKey(District, blank=False, null=False, related_name='shops')
    category = models.ForeignKey(ClientCategory, blank=True, null=True, related_name='shops')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self.client.name, self.name, self.type, self.city, self.address)
