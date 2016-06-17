# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0011_auto_20151230_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinformation',
            name='first_check',
            field=models.CharField(default='not_checked', max_length=50, choices=[('VAR', 'variant'), ('POL', 'polymorphism'), ('ART', 'artefact')]),
        ),
        migrations.AlterField(
            model_name='sampleinformationauditlogentry',
            name='first_check',
            field=models.CharField(default='not_checked', max_length=50, choices=[('VAR', 'variant'), ('POL', 'polymorphism'), ('ART', 'artefact')]),
        ),
    ]
