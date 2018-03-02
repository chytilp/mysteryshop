# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('recorded', models.DateTimeField(editable=False, verbose_name='recorded when', default=django.utils.timezone.now)),
                ('data', models.FileField(upload_to='data', verbose_name='data file')),
                ('file_name', models.CharField(max_length=100, verbose_name='name of data file')),
                ('type', models.CharField(max_length=10, verbose_name='type of data file')),
                ('interviewer', models.ForeignKey(to='account.Interviewer', related_name='attachments', verbose_name='interviewer')),
                ('shop', models.ForeignKey(to='project.Shop', related_name='attachments', verbose_name='shop')),
                ('wave', models.ForeignKey(to='project.Wave', related_name='attachments', verbose_name='wave')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=7, verbose_name='amount of money', decimal_places=2)),
                ('description', models.TextField(verbose_name='description')),
                ('interviewer', models.ForeignKey(to='account.Interviewer', related_name='bonuses', verbose_name='interviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('score', models.PositiveSmallIntegerField(verbose_name='test score')),
                ('passed', models.DateTimeField(blank=True, verbose_name='test was passed when', null=True)),
                ('interviewer', models.ForeignKey(to='account.Interviewer', related_name='tests', verbose_name='interviewer')),
                ('project', models.ForeignKey(to='project.Project', related_name='tests', verbose_name='project')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('group', models.PositiveIntegerField(verbose_name='group of shops')),
                ('date_from', models.DateField(verbose_name='visit from date')),
                ('date_to', models.DateField(verbose_name='visit to date')),
                ('visit_day', models.DateField(blank=True, verbose_name='visit date', null=True)),
                ('is_pm', models.NullBooleanField(verbose_name='is pm time')),
                ('data', jsonfield.fields.JSONField(blank=True, verbose_name='questionnaire data', null=True)),
                ('data_recorded', models.DateTimeField(blank=True, verbose_name='data recorded when', null=True)),
                ('interviewer', models.ForeignKey(blank=True, to='account.Interviewer', null=True, related_name='visits', verbose_name='interviewer')),
                ('shop', models.ForeignKey(to='project.Shop', related_name='visits', verbose_name='shop')),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('billing_period', models.DateField(verbose_name='billing period')),
                ('amount', models.DecimalField(max_digits=7, verbose_name='amount of money', decimal_places=2)),
                ('description', models.TextField(blank=True, verbose_name='description', null=True)),
                ('requested', models.DateTimeField(editable=False, verbose_name='description', default=django.utils.timezone.now)),
                ('paid', models.BooleanField(verbose_name='wage was paid', default=False)),
                ('interviewer', models.ForeignKey(to='account.Interviewer', related_name='wages', verbose_name='interviewer')),
            ],
        ),
        migrations.AddField(
            model_name='visit',
            name='wage',
            field=models.ForeignKey(blank=True, to='visit.Wage', null=True, related_name='visits', verbose_name='wage'),
        ),
        migrations.AddField(
            model_name='visit',
            name='wave',
            field=models.ForeignKey(to='project.Wave', related_name='visits', verbose_name='wave'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='wage',
            field=models.ForeignKey(blank=True, to='visit.Wage', null=True, related_name='bonuses', verbose_name='wage'),
        ),
        migrations.AddField(
            model_name='bonus',
            name='wave',
            field=models.ForeignKey(to='project.Wave', related_name='bonuses', verbose_name='wave'),
        ),
    ]
