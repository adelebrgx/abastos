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

            slug=product+"-"+quantity

            sell.save()

            for p in products:
                #print(p.id)
                #print(product)
                if p.name==product:

                    sellPair = SellPair.objects.create(sell=sell,quantity=quantity, product=p, slug=slug)
                    sellPair.save()
            return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user})

    return render(request, 'sell/publish.html', {'user':request.user, 'products': products, 'locations':locations})


def sell_details(request, slug):

    sell= SellPair.objects.get(slug=slug)
    sells=Sell.objects.all().order_by('name')
    sellPairs= SellPair.objects.all().order_by('product')
    user=request.user
    if user.is_anonymous():
        print("anonymous")
        locations=None

    else:
        locations=Location.objects.filter(owner=user)
    products=Product.objects.all().order_by('name')

    if request.method=="POST":
        product_name=request.POST.get('product')
        new_product= Product.objects.get(name=product_name)
        location_name=request.POST.get('location')
        new_location=Location.objects.get(name=location_name)
        new_quantity=request.POST.get('quantity')
        #print(new_product)
        #print(new_location)
        #print(new_quantity)
        #print(sell.sell.location)
        sell.product=new_product
        sell.quantity=new_quantity
        sell_associated=sell.sell
        sell_associated.location=new_location
        sell.save()
        sell_associated.save()
        #sell.product=new_product

        return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user})
    #print(sell)
    return render(request, 'sell/sell_details.html',  {'user':user, 'sellPair':sell, 'locations':locations, 'products': products})


def sell_delete(request,slug):
    sellpair= SellPair.objects.get(slug=slug)

    sellpairs_list=SellPair.objects.all().order_by('product')
    print(sellpair)
    sellpair.delete()
    sells=Sell.objects.all().order_by('name')
    user=request.user
    return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellpairs_list,'user':request.user})
