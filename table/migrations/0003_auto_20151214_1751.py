# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20151214_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinformation',
            name='first_check',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sampleinformationauditlogentry',
            name='first_check',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
