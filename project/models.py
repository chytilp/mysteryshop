from django.db import models
from django.utils.translation import ugettext_lazy as _l

from model_utils import Choices

from utils.models.mixins import ActiveFieldMixin, SimpleEnumClassMixin


class Region(models.Model, SimpleEnumClassMixin):

    name = models.CharField(verbose_name=_l('name'), blank=False, null=False, max_length=20)
    slug = models.SlugField(verbose_name=_l('slug'), blank=False, null=False, max_length=5)


class District(models.Model, SimpleEnumClassMixin):

    name = models.CharField(verbose_name=_l('name'), blank=False, null=False, max_length=20)
    region = models.ForeignKey(Region, verbose_name=_l('region'), blank=False, null=False, related_name='districts')
    slug = models.SlugField(verbose_name=_l('slug'), blank=False, null=False, max_length=10)


class Client(models.Model, SimpleEnumClassMixin):

    name = models.CharField(verbose_name=_l('name'), blank=False, null=False, max_length=50)
    description = models.TextField(verbose_name=_l('description'), blank=True, null=True)
    slug = models.SlugField(verbose_name=_l('slug'), blank=False, null=False, max_length=20)


class Project(ActiveFieldMixin, SimpleEnumClassMixin):

    name = models.CharField(verbose_name=_l('name'), blank=False, null=False, max_length=50)
    number = models.PositiveIntegerField(verbose_name=_l('project number'), blank=False, null=False)
    client = models.ForeignKey(Client, verbose_name=_l('client'), blank=False, null=False, related_name='projects')
    date_from = models.DateField(verbose_name=_l('project start date'), blank=False, null=False)
    date_to = models.DateField(verbose_name=_l('project end date'), blank=True, null=True)
    test_cluster = models.PositiveIntegerField(verbose_name=_l('project test cluster'), blank=True, null=True)
    limit_for_test = models.PositiveIntegerField(verbose_name=_l('project limit for passing test'), blank=True,
                                                 null=True)


class Wave(models.Model):

    STATUS = Choices(
        (1, 'PREPARING', _l('Preparing')),  # can see admin, interviewer not yet
        (2, 'ACTIVE', _l('Active')),        # interviewer can see it
        (3, 'FINISHED', _l('Finished')),    # lock for interviewer changes
        (4, 'CLOSED', _l('Closed')),        # move to archive
    )

    number = models.PositiveIntegerField(verbose_name=_l('wave number'), blank=False, null=False)
    project = models.ForeignKey(Project, verbose_name=_l('project'), blank=False, null=False, related_name='waves')
    date_from = models.DateField(verbose_name=_l('wave start date'), blank=False, null=False)
    date_to = models.DateField(verbose_name=_l('wave end date'), blank=False, null=False)
    status = models.PositiveIntegerField(verbose_name=_l('status'), choices=STATUS, default=STATUS.PREPARING)
    fee_full = models.DecimalField(verbose_name=_l('wave full fee'), max_digits=10, decimal_places=2, blank=True,
                                   null=True)
    fee_part = models.DecimalField(verbose_name=_l('wave part fee'), max_digits=10, decimal_places=2, blank=True,
                                   null=True)
    max_delay_for_full_fee = models.PositiveIntegerField(verbose_name=_l('max delay for full fee'), blank=True,
                                                         null=True, default=0)

    def __str__(self):
        return 'Project: {}, wave: {}'.format(self.project.name, str(self.number))


class Shop(ActiveFieldMixin):

    name = models.CharField(verbose_name=_l('name'), blank=False, null=False, max_length=50)
    client_shop_id = models.CharField(verbose_name=_l('client shop identifier'), blank=False, null=False,
                                      max_length=10, default='')
    client = models.ForeignKey(Client, verbose_name=_l('client'), blank=False, null=False, related_name='shops')
    district = models.ForeignKey(District, verbose_name=_l('district'), blank=False, null=False, related_name='shops')
    category = models.CharField(verbose_name=_l('category'), blank=True, null=True, max_length=50)
    city = models.CharField(verbose_name=_l('city'), blank=True, null=True, max_length=100)
    address = models.CharField(verbose_name=_l('address'), blank=True, null=True, max_length=100)
    zip_code = models.PositiveSmallIntegerField(verbose_name=_l('zip code'), blank=True, null=True)

    def __str__(self):
        return '{}-{}-{}-{}-{}'.format(self.client.name, self.name, self.type, self.city, self.address)
