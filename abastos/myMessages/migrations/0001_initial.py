# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-17 01:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='myMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('head', models.CharField(max_length=50)),
                ('content', models.CharField(default='This message is empty', max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
