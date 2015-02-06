# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dark', '0003_auto_20150202_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facecard',
            name='ability',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facecard',
            name='advantage_1',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facecard',
            name='advantage_2',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facecard',
            name='advantage_3',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sheet',
            name='name',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
