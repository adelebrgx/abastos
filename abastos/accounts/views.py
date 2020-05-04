# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.models import User

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
    return render(request, 'accounts/signup.html', {'form':form,'user':request.user})


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
    return render(request, 'accounts/login.html', {'form':form,'user':request.user})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('/homepage')

def infos_view(request):
    user=request.user
    identicals=True
    password=True

    if request.method=="POST":
        myName=request.POST.get('firstname')
        myLastName=request.POST.get('lastname')
        new1=request.POST.get('new1')
        new2=request.POST.get('new2')
        myEmailAdress=request.POST.get('email')

        user=User.objects.get(username=user.username)

        #print(new1)
        #print(new2)
        if (str(new1)=="" or str(new2)==""):
            print("password wasn't changed")
            password=False

            render(request, "accounts/infos.html", {'user':user, 'identicals':identicals, 'password':password})
        elif(str(new1)!=str(new2)):
            print("password aren't identicals")
            identicals=False

            return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'password':password})
        else:
            user.set_password(new2)
            print("password was changed to")
            print(new2)
            user.last_name=myLastName
            user.first_name=myName
            user.email=myEmailAdress
            user.save()
            return redirect('/homepage')
    return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals, 'password':password})
