# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-23 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0005_auto_20161117_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='schoolOfWork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.School'),
        ),
    ]
