# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-11 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0106_auto_20180611_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalaccount',
            name='encrypted',
            field=models.BooleanField(default=True),
        ),
    ]