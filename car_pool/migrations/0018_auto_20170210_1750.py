# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-10 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0017_auto_20170209_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='seats',
        ),
        migrations.AddField(
            model_name='journey',
            name='available_seats',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.Destination0ptions'),
        ),
    ]
