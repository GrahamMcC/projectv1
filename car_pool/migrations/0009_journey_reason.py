# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0008_auto_20170125_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='reason',
            field=models.TextField(default='no reason given'),
        ),
    ]
