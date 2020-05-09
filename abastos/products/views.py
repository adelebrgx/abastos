# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from sell.models import SellPair
from .import forms
from django.http import HttpResponse
import re
from urlparse import urlparse

def products_list_view(request):
    products=Product.objects.all().order_by('name')
    sellpairs=SellPair.objects.all().order_by('product')
    return render(request, "products/productslist.html",{'products':products, 'sellpairs':sellpairs} )

@login_required(login_url="/accounts/login/")
def publish(request):
    isName=True
    isUrl=True
    notAlreadyExists=True
    sellpairs_list=SellPair.objects.all().order_by('product')
    if request.method=="POST":
        products=Product.objects.all().order_by('name')
        name=request.POST.get('name')
        url=request.POST.get('url')
        already=Product.objects.filter(name=name).count()
        if(already!=0):
            notAlreadyExists=False
        if(correct_name(name)==False):
            isName=False
        if(correct_url(url)==False):
            isUrl=False
        if(correct_name(name)==True and correct_url(url)==True and notAlreadyExists==True):
            product=Product.objects.create(name=name, url=url)
            product.save()
            return render(request, 'products/productslist.html', {'products':products,'user':request.user, 'sellpairs':sellpairs_list})
        else:
            return render(request, 'products/publish.html', {'user':request.user,'isName': isName, 'isUrl':isUrl, 'notAlreadyExists':notAlreadyExists})

    return render(request, 'products/publish.html', {'user':request.user,'isName': isName, 'isUrl':isUrl,'notAlreadyExists':notAlreadyExists})


def correct_name(s):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
    if(regex.search(s) == None):
        return True
    return False

def correct_url(url):
    result=urlparse(url)
    if(result.scheme!= "" and result.netloc!=""):
        return True
    return False

def product_details(request,slug):
    isName=True
    isUrl=True
    notAlreadyExists=True
    products=Product.objects.all().order_by('name')
    sellpairs_list=SellPair.objects.all().order_by('product')
    user=request.user
    if request.method=='POST':
        product= Product.objects.get(name=slug)
        new_name=request.POST.get('name')
        new_url=request.POST.get('url')
        if (correct_name(new_name)==False):
            isName=False
        if(correct_url(new_url)==False):
            isUrl=False
        already=Product.objects.filter(name=new_name).count()
        if(already!=0):
            if(new_name!=product.name):
                notAlreadyExists=False
        if(isName==True and isUrl==True and notAlreadyExists==True):
            product.name=new_name
            product.url=new_url
            product.save()
            return render(request, 'products/productslist.html', {'products':products,'user':request.user, 'sellpairs':sellpairs_list})
        else:
            return render(request, 'products/product_details.html', {'product':product,'user':request.user,'isName': isName, 'isUrl':isUrl,'notAlreadyExists':notAlreadyExists})
    product= Product.objects.get(name=slug)
    return render (request, 'products/product_details.html', {'product':product, 'user':user,'isName': isName, 'isUrl':isUrl, 'notAlreadyExists':notAlreadyExists})

def product_delete(request,slug):
    product= Product.objects.get(name=slug)
    sellpairs=SellPair.objects.filter(product=product)
    sellpairs_list=SellPair.objects.all().order_by('product')
    print(product)
    for s in sellpairs:
        s.delete()
    product.delete()
    products=Product.objects.all().order_by('name')
    user=request.user
    return render(request, 'products/productslist.html', {'products':products,'user':request.user, 'sellpairs':sellpairs_list})
