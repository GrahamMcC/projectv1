# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-13 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0020_auto_20170213_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='available_seats',
            field=models.SmallIntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.Destination0ptions'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='reason',
            field=models.CharField(default='What is the reason for this journey', max_length=20),
        ),
    ]
