# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_auto_20151215_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinformation',
            name='first_check',
            field=models.CharField(default=b'not_checked', max_length=50),
        ),
        migrations.AlterField(
            model_name='sampleinformation',
            name='second_check',
            field=models.CharField(default=b'not_checked', max_length=50),
        ),
        migrations.AlterField(
            model_name='sampleinformationauditlogentry',
            name='first_check',
            field=models.CharField(default=b'not_checked', max_length=50),
        ),
        migrations.AlterField(
            model_name='sampleinformationauditlogentry',
            name='second_check',
            field=models.CharField(default=b'not_checked', max_length=50),
        ),
    ]
