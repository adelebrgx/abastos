# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sell, SellPair
from products.models import Product
from locations.models import Location
from .import forms

def sell_list_view(request):
    sellPairs=SellPair.objects.all().order_by('product')

    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user})

@login_required(login_url="/accounts/login/")
def publish(request):
    sellPairs=SellPair.objects.all().order_by('product')
    sells=Sell.objects.all().order_by('date')
    user=request.user
    products=Product.objects.all().order_by('name')
    locations=Location.objects.filter(owner=user)
    if request.method=="POST":

            user=request.user
            quantity=request.POST.get('quantity')
            product=request.POST.get('product')


            location_name=request.POST.get('location')
            location=Location.objects.get(name=location_name)


            sell=Sell.objects.create(author=user,location=location)

            slug=product+"-"+quantity+"-"+str(sell.date)

            sell.save()

            for p in products:
                print(p.id)
                print(product)
                if p.name==product:

                    sellPair = SellPair.objects.create(sell=sell,quantity=quantity, product=p, slug=slug)
                    sellPair.save()



            #
            #sellPair.save()
            return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user})

    return render(request, 'sell/publish.html', {'user':request.user, 'products': products, 'locations':locations})
