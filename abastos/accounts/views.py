# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/success')
    else:
        form=UserCreationForm()
    form=UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def success_view(request):
    return render(request, 'accounts/success.html')
