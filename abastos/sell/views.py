# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sell, SellPair
from products.models import Product
from .import forms

def sell_list_view(request):
    sellPairs=SellPair.objects.all().order_by('product')
    print (sellPairs[0].sell.date)
    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs})

def publish(request):
    form=forms.CreateSell()
    return render(request, 'sell/publish.html', {'form':form})
