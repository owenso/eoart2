# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20171223_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='me/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='bio',
            options={},
        ),
    ]
