# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acecard',
            name='suit',
            field=models.OneToOneField(related_name='ace', to='dark.Suit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basecard',
            name='suit',
            field=models.OneToOneField(related_name='base_card', to='dark.Suit'),
            preserve_default=True,
        ),
    ]
