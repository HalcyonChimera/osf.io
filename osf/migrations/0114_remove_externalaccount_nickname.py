# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0113_merge_20180620_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalaccount',
            name='nickname',
        ),
    ]
