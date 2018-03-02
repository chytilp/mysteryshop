# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', models.TextField(verbose_name='content')),
                ('title', models.CharField(verbose_name='title', max_length=100)),
                ('sent_when', models.DateTimeField(null=True, blank=True, editable=False, verbose_name='sent when')),
                ('status', models.PositiveIntegerField(choices=[(1, 'New'), (2, 'Assign'), (3, 'In progress'), (4, 'Solved'), (5, 'Unsolvable')], verbose_name='status', default=1)),
                ('current_status_from', models.DateTimeField(null=True, blank=True, verbose_name='current status from', default=django.utils.timezone.now)),
                ('related_communication_id', models.PositiveIntegerField(blank=True, verbose_name='related communication id', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageContext',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(related_name='message_contexts', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
                ('project', models.ForeignKey(related_name='message_contexts', blank=True, to='project.Project', null=True, verbose_name='project')),
                ('wave', models.ForeignKey(related_name='message_contexts', blank=True, to='project.Wave', null=True, verbose_name='wave')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='context',
            field=models.ForeignKey(related_name='messages', blank=True, to='message.MessageContext', null=True, verbose_name='message context'),
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(related_name='from_messages', to=settings.AUTH_USER_MODEL, verbose_name='from user'),
        ),
        migrations.AddField(
            model_name='message',
            name='solver',
            field=models.ForeignKey(related_name='solver_messages', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='solver'),
        ),
        migrations.AddField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(related_name='to_messages', to=settings.AUTH_USER_MODEL, verbose_name='to user'),
        ),
    ]
