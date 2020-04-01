# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=20)
    url=models.CharField(max_length=1000,default="foobar")

    def __str__(self):
        return self.name
