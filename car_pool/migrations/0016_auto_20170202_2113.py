# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-02 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0015_auto_20170202_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.Destination0ptions'),
        ),
    ]
