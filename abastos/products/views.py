# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product

def products_list_view(request):
    products=Product.objects.all().order_by('name')
    return render(request, "products/productslist.html",{'products':products} )
