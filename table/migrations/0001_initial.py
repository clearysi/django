# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100000000)),
                ('sender', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=50)),
                ('response', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SampleInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('d_number', models.CharField(unique=True, max_length=10)),
                ('date', models.DateField()),
                ('worksheet_number', models.CharField(max_length=6)),
                ('link', models.CharField(max_length=500)),
                ('first_check', models.CharField(max_length=10)),
                ('second_check', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SampleInformationAuditLogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('d_number', models.CharField(max_length=10, db_index=True)),
                ('date', models.DateField()),
                ('worksheet_number', models.CharField(max_length=6)),
                ('link', models.CharField(max_length=500)),
                ('first_check', models.CharField(max_length=10)),
                ('second_check', models.CharField(max_length=10)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_sampleinformation_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload', models.FileField(upload_to=b'/home/scleary/django_projects/files')),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='table',
            field=models.ForeignKey(to='table.SampleInformation'),
        ),
    ]
