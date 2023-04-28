# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 11:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wallet.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0003_owner_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Only 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('type', models.CharField(choices=[('PREPAID', 'PREPAID'), ('POSTPAID', 'POSTPAID')], max_length=10)),
                ('operator', models.CharField(choices=[('RELIANCE', 'RELIANCE'), ('TATA DOCOMO', 'TATA DOCOMO'), ('VODAFONE', 'VODAFONE'), ('IDEA', 'IDEA'), ('MTNL', 'MTNL'), ('AIRCEL', 'AIRCEL'), ('AIRTEL', 'AIRTEL'), ('MTS', 'MTS')], max_length=15)),
                ('circle', models.CharField(choices=[('MUMBAI', 'MUMBAI'), ('DELHI', 'DELHI'), ('GUJARAT', 'GUJARAT'), ('HARYANA', 'HARYANA'), ('KOLKATA', 'KOLKATA'), ('PUNJAB', 'PUNJAB'), ('RAJASTHAN', 'RAJASTHAN'), ('TAMILNADU', 'TAMILNADU'), ('KERALA', 'KERALA'), ('JAMMU AND KASHMIR', 'JAMMU AND KASHMIR')], max_length=20)),
                ('plan', models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50')], max_length=50)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, wallet.models.Main),
        ),
    ]