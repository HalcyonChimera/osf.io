# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-18 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0107_externalaccount_encrypted'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='externalaccount',
            unique_together=set([('provider', 'provider_id', 'host', 'port')]),
        ),
    ]
