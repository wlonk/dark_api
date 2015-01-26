# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AceCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FaceCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('value', models.IntegerField(default=4)),
                ('ability', models.CharField(max_length=128)),
                ('advantage_1', models.CharField(max_length=128)),
                ('advantage_2', models.CharField(max_length=128)),
                ('advantage_3', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('look', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('apt', models.BooleanField(default=False)),
                ('edu', models.BooleanField(default=False)),
                ('exp', models.BooleanField(default=False)),
                ('acc', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('sheet', models.ForeignKey(to='dark.Sheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('sheet', models.ForeignKey(to='dark.Sheet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_group',
            field=models.ForeignKey(to='dark.SkillGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facecard',
            name='suit',
            field=models.ForeignKey(to='dark.Suit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basecard',
            name='suit',
            field=models.ForeignKey(to='dark.Suit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acecard',
            name='suit',
            field=models.ForeignKey(to='dark.Suit'),
            preserve_default=True,
        ),
    ]
