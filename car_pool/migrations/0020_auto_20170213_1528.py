# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-13 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0019_auto_20170212_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.Destination0ptions'),
        ),
    ]