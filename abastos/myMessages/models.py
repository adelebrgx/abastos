# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class myMessage(models.Model):
    id = models.AutoField(primary_key=True)
    head=models.CharField(max_length=50)
    content=models.CharField(max_length=1000,default="This message is empty")
    author=models.ForeignKey(User, related_name="from+")
    recipient=models.ForeignKey(User, related_name="to+")
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.head+" from "+ str(self.author)+" to "+str(self.recipient)
