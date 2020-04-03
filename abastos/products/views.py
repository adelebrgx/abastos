# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product
from .import forms

def products_list_view(request):
    products=Product.objects.all().order_by('name')
    return render(request, "products/productslist.html",{'products':products} )

def publish(request):
    if request.method=="POST":
        products=Product.objects.all().order_by('name')
        form=forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            name=request.POST['name']
            url=request.POST['url']
            product=Product.objects.create(name=name, url=url)
            product.save()

            return render(request, 'products/productslist.html', {'products':products,'user':request.user})
    else:
        form=forms.CreateProduct()
    return render(request, 'products/publish.html', {'form':form,'user':request.user})
