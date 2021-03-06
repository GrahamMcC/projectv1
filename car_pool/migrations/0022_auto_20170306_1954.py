# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-06 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_pool', '0021_auto_20170213_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='homeCampus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car_pool.Origin0ptions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='numberOfSeats',
            field=models.IntegerField(default='5'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_pool.Destination0ptions'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='reason',
            field=models.CharField(default='Why are you traveling', max_length=20),
        ),
    ]
