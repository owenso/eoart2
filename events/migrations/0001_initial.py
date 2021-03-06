# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('venue_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateTimeField(blank=True, null=True)),
                ('endDate', models.DateTimeField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('show_image', models.ImageField(blank=True, null=True, upload_to='shows/')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
