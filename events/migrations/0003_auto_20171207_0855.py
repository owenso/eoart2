# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171205_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='previousvenue',
            options={'ordering': ['venue_name']},
        ),
    ]
