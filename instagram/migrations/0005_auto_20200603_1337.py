# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-03 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20200603_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='liked_image',
        ),
        migrations.RemoveField(
            model_name='like',
            name='likers',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
