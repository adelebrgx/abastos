# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse

def buy_list_view(request):
    return render(request,'buy/buylist.html',{'user':request.user})
