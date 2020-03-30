# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

def sell_list_view(request):
    return render(request,'sell/selllist.html')
