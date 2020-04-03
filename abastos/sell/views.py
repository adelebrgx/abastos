# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sell, SellPair
from products.models import Product
from .import forms

def sell_list_view(request):
    sellPairs=SellPair.objects.all().order_by('product')
    print (sellPairs[0].sell.date)
    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user})

@login_required(login_url="/accounts/login/")
def publish(request):
    sellPairs=SellPair.objects.all().order_by('product')
    sells=Sell.objects.all().order_by('date')
    products=Product.objects.all().order_by('name')
    if request.method=="POST":
        form=forms.CreateSell(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            quantity=request.POST['quantity']
            product=request.POST['product']
            #print(product)
            sell=Sell.objects.create(author=user)
            print(sell)
            #sell.save()
            #effective_product=Product.objects.create(name="unknown",url="unknown")
            for p in products:
                print(p.id)
                print(product)
                if int(p.id)==int(product):
                    print("hello")
                    sellPair = SellPair.objects.create(sell=sell,quantity=quantity, product=p)
                    sellPair.save()
                    print(sellPair)
                    print(sellPair.sell)


            #
            #sellPair.save()
            return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user})
    else:
        form=forms.CreateSell()
    return render(request, 'sell/publish.html', {'form':form,'user':request.user})
