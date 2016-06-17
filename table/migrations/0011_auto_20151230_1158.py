# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_auto_20151218_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinformation',
            name='first_check',
            field=models.CharField(max_length=50, choices=[(b'VAR', b'variant'), (b'POL', b'polymorphism'), (b'ART', b'artefact')]),
        ),
        migrations.AlterField(
            model_name='sampleinformationauditlogentry',
            name='first_check',
            field=models.CharField(max_length=50, choices=[(b'VAR', b'variant'), (b'POL', b'polymorphism'), (b'ART', b'artefact')]),
        ),
    ]
