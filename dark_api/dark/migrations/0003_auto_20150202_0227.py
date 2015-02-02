# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dark', '0002_auto_20150126_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='look',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
