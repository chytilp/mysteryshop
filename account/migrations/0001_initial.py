# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.cz_models.fields
import utils.models.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='first name')),
                ('personal_id', libs.cz_models.fields.CZBirthNumberField(max_length=11, verbose_name='personal id', blank=True, null=True)),
                ('phone', utils.models.fields.PhoneNumberField(verbose_name='phone')),
                ('is_man', models.BooleanField(verbose_name='is man')),
                ('districts', models.TextField(verbose_name='working districts')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('zip_code', models.PositiveSmallIntegerField(verbose_name='zip code')),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, 'New'), (2, 'In progress'), (3, 'Approved')], verbose_name='status')),
                ('education', models.PositiveIntegerField(choices=[(1, 'Basic'), (2, 'Secondary'), (3, 'Secondary graduated'), (4, 'College')], verbose_name='education')),
                ('registered', models.DateTimeField(editable=False, default=django.utils.timezone.now, verbose_name='registered')),
                ('status_change_when', models.DateTimeField(verbose_name='status was changed when', blank=True, null=True)),
                ('cancel_reason', models.TextField(verbose_name='reason of cancellation', blank=True, null=True)),
                ('status_change_by', models.ForeignKey(null=True, related_name='candidates', to=settings.AUTH_USER_MODEL, blank=True, verbose_name='status was changed by')),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', utils.models.fields.PhoneNumberField(verbose_name='phone', blank=True, null=True)),
                ('bank_account', libs.cz_models.fields.BankAccountNumber(max_length=24, verbose_name='bank account number', blank=True, null=True)),
                ('user', models.OneToOneField(related_name='interviewer', to=settings.AUTH_USER_MODEL, verbose_name='app user')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewerDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_home', models.BooleanField(default=False, verbose_name='is home district')),
                ('district', models.ForeignKey(related_name='interviewers', to='project.District', verbose_name='district')),
                ('interviewer', models.ForeignKey(related_name='districts', to='account.Interviewer', verbose_name='interviewer')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, 'Unapproved'), (2, 'Cancelled'), (3, 'Active'), (4, 'Paused'), (5, 'Finished')], verbose_name='status')),
                ('begin', models.DateTimeField(verbose_name='begin date')),
                ('interviewer', models.ForeignKey(related_name='statuses', to='account.Interviewer', verbose_name='interviewer')),
            ],
        ),
        migrations.AddField(
            model_name='interviewer',
            name='visit_districts',
            field=models.ManyToManyField(to='project.District', through='account.InterviewerDistrict', verbose_name='working districts'),
        ),
    ]
