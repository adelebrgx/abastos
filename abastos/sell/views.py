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
    type="product"
    sellPairs=SellPair.objects.all().order_by('product')
    sells=Sell.objects.all().order_by('author')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user, 'type':type})

def sell_list_by_date(request):
    type="date"
    sellPairs=SellPair.objects.all().order_by('sell__date')
    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user, 'type':type})

def sell_list_by_location(request):
    type="location"
    sellPairs=SellPair.objects.all().order_by('sell__location')
    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user, 'type':type})


def sell_list_by_author(request):
    type="author"
    sellPairs=SellPair.objects.all().order_by('sell__author')
    sells=Sell.objects.all().order_by('date')
    return render(request,'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs, 'user':request.user, 'type':type})


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

            sell.save()

            slug=product+"-"+quantity
            for p in products:
                if p.name==product:
                    sellPair = SellPair.objects.create(sell=sell,quantity=quantity, product=p, slug=slug)
                    sellPair.save()

            if str(request.POST.get('quantity-1'))!="":
                quantity1=request.POST.get('quantity-1')
                product1=request.POST.get('product-1')
                slug1=product1+"-"+quantity1
                print(slug1)
                for p in products:
                    if p.name==product1:
                        sellPair1 = SellPair.objects.create(sell=sell,quantity=quantity1, product=p, slug=slug1)
                        sellPair1.save()
            if str(request.POST.get('quantity-2'))!="":
                quantity2=request.POST.get('quantity-2')
                product2=request.POST.get('product-2')
                slug2=product2+"-"+quantity2
                print(slug2)
                for p in products:
                    if p.name==product2:
                        sellPair2 = SellPair.objects.create(sell=sell,quantity=quantity2, product=p, slug=slug2)
                        sellPair2.save()
            if str(request.POST.get('quantity-3'))!="":
                quantity3=request.POST.get('quantity-3')
                product3=request.POST.get('product-3')
                slug3=product3+"-"+quantity3
                print(slug3)
                for p in products:
                    if p.name==product3:
                        sellPair3 = SellPair.objects.create(sell=sell,quantity=quantity3, product=p, slug=slug3)
                        sellPair3.save()
            if str(request.POST.get('quantity-4'))!="":
                quantity4=request.POST.get('quantity-4')
                product4=request.POST.get('product-4')
                slug4=product4+"-"+quantity4
                print(slug4)
                for p in products:
                    if p.name==product4:
                        sellPair4 = SellPair.objects.create(sell=sell,quantity=quantity4, product=p, slug=slug4)
                        sellPair4.save()




            type="product"
            return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user,'type':type})

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
        sell.slug=str(new_product)+"-"+str(new_quantity)
        sell_associated=sell.sell
        sell_associated.location=new_location
        sell.save()
        sell_associated.save()
        #sell.product=new_product

        type="product"
        return render(request, 'sell/selllist.html', {'sells':sells, 'sellpairs': sellPairs,'user':request.user,'type':type})
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
