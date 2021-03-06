# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20171223_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentshow',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='currentshow',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='currentshow',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='currentshow',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
