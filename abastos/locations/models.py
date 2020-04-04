# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    north_coordinate=models.FloatField()
    east_coordinate=models.FloatField()
    owner=models.ForeignKey(User)
    slug=models.CharField(max_length=50, default="none")

    def __str__(self):
        return self.name
