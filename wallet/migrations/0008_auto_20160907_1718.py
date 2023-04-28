# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_auto_20160907_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='plan',
            field=models.IntegerField(choices=[(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)], max_length=2),
        ),
    ]
