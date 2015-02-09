# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dark', '0004_auto_20150206_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='available_xp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
