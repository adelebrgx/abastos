# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product
from .import forms
from django.http import HttpResponse

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

def product_details(request,slug):
    products=Product.objects.all().order_by('name')
    user=request.user
    if request.method=='POST':

        product= Product.objects.get(name=slug)
        print(request.POST.get('name'))
        new_name=request.POST.get('name')

        new_url=request.POST.get('url')
        print(new_url)
        product.name=new_name
        product.url=new_url
        product.save()
        return render(request, 'products/productslist.html', {'products':products,'user':request.user})
    product= Product.objects.get(name=slug)
    return render (request, 'products/product_details.html', {'product':product, 'user':user})
