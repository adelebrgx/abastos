# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-04 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='location',
        ),
    ]
