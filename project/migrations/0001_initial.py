# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.models.mixins


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True, null=True)),
                ('slug', models.SlugField(max_length=20, verbose_name='slug')),
            ],
            bases=(models.Model, utils.models.mixins.SimpleEnumClassMixin),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('slug', models.SlugField(max_length=10, verbose_name='slug')),
            ],
            bases=(models.Model, utils.models.mixins.SimpleEnumClassMixin),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.DateField(default=None, blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('number', models.PositiveIntegerField(verbose_name='project number')),
                ('date_from', models.DateField(verbose_name='project start date')),
                ('date_to', models.DateField(verbose_name='project end date', blank=True, null=True)),
                ('test_cluster', models.PositiveIntegerField(verbose_name='project test cluster', blank=True, null=True)),
                ('limit_for_test', models.PositiveIntegerField(verbose_name='project limit for passing test', blank=True, null=True)),
                ('client', models.ForeignKey(related_name='projects', to='project.Client', verbose_name='client')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, utils.models.mixins.SimpleEnumClassMixin),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('slug', models.SlugField(max_length=5, verbose_name='slug')),
            ],
            bases=(models.Model, utils.models.mixins.SimpleEnumClassMixin),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.DateField(default=None, blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('client_shop_id', models.CharField(max_length=10, default='', verbose_name='client shop identifier')),
                ('category', models.CharField(max_length=50, verbose_name='category', blank=True, null=True)),
                ('city', models.CharField(max_length=100, verbose_name='city', blank=True, null=True)),
                ('address', models.CharField(max_length=100, verbose_name='address', blank=True, null=True)),
                ('zip_code', models.PositiveSmallIntegerField(verbose_name='zip code', blank=True, null=True)),
                ('client', models.ForeignKey(related_name='shops', to='project.Client', verbose_name='client')),
                ('district', models.ForeignKey(related_name='shops', to='project.District', verbose_name='district')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='wave number')),
                ('date_from', models.DateField(verbose_name='wave start date')),
                ('date_to', models.DateField(verbose_name='wave end date')),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, 'Preparing'), (2, 'Active'), (3, 'Finished'), (4, 'Closed')], verbose_name='status')),
                ('fee_full', models.DecimalField(max_digits=10, verbose_name='wave full fee', blank=True, decimal_places=2, null=True)),
                ('fee_part', models.DecimalField(max_digits=10, verbose_name='wave part fee', blank=True, decimal_places=2, null=True)),
                ('max_delay_for_full_fee', models.PositiveIntegerField(verbose_name='max delay for full fee', default=0, blank=True, null=True)),
                ('project', models.ForeignKey(related_name='waves', to='project.Project', verbose_name='project')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(related_name='districts', to='project.Region', verbose_name='region'),
        ),
    ]
