# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0022_auto_20160910_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
