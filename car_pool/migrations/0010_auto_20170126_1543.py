# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0009_journey_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='reason',
            field=models.TextField(default='please give a reason for the journey', max_length=30),
        ),
    ]
