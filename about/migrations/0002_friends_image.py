# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='image',
            field=models.ImageField(default='http://fillmurray.com/500/500', upload_to='friends/'),
            preserve_default=False,
        ),
    ]