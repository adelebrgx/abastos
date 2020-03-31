# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,  authenticate, logout

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/accounts/success')
    else:
        form=UserCreationForm()
    form=UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def success_view(request):
    return render(request, 'accounts/success.html')

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        data=request.POST
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)
        print(user)
        if form.is_valid:


            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('/homepage')
