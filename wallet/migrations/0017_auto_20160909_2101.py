# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0016_auto_20160909_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recharge',
            options={'ordering': ['-timestamp']},
        ),
    ]
