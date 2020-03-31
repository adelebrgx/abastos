# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import Product
from django.db import models
from django.contrib.auth.models import User

class Sell(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User)

    def __str__(self):
        return self.author.username +' '+ str(self.date)


class SellPair(models.Model):
    sell=models.ForeignKey(Sell,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name +" "+ str(self.quantity)
