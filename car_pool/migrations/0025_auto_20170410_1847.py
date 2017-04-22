# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-10 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0024_auto_20170408_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='cost',
        ),
        migrations.AddField(
            model_name='journey',
            name='cost_per_person',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='journey',
            name='total_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='journey',
            name='distance',
            field=models.FloatField(default=0),
        ),
    ]