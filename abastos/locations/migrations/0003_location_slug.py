# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-03 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20200403_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
