# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.models import User

import re

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

def num_there(s):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
    if(regex.search(s) == None):
        return False
    return True


def infos_view(request):
    user=request.user
    identicals=True
    email=True
    lastname=True
    name=True
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


    if request.method=="POST":
        myName=request.POST.get('firstname')
        myLastName=request.POST.get('lastname')
        new1=request.POST.get('new1')
        new2=request.POST.get('new2')
        myEmailAdress=request.POST.get('email')
        user=User.objects.get(username=user.username)

        #wishes to reset password
        if(str(new1)==str(new2) and str(new1)!=""):
            if(re.search(regex,myEmailAdress)):
                if(num_there(myLastName)==True):
                    print("lastname ok")
                user.last_name=myLastName
                user.first_name=myName
                user.email=myEmailAdress
                user.set_password(new2)
                user.save()
                return redirect('/homepage')
            else:
                email=False
                return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email, 'name':name,'lastname':lastname})

        #doesn't wish to reset password correct
        elif(str(new1)=="" and str(new2)==""):

            print(num_there(myLastName))
            print(num_there(myName))

            if(re.search(regex,myEmailAdress)):
                #if(num_there(myLastName)==False):
                if(num_there(myLastName)==False):
                    if(num_there(myName)==False):
                        user.email=myEmailAdress
                        user.last_name=myLastName
                        user.first_name=myName
                        user.save()
                        return redirect('/homepage')
                    name=False
                    return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email, 'name':name,'lastname':lastname})
                lastname=False
                if(num_there(myName)==True):
                    name=False
                return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email, 'name':name,'lastname':lastname})



            else:
                print("not valid email adress")
                email=False
                if(num_there(myName)==True):
                    name=False
                if(num_there(myLastName)==True):
                    lastname=False
                return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email, 'name':name,'lastname':lastname})



        #wishes to reset password incorrect
        else:
            if(str(re.search(regex,myEmailAdress))=="None"):
                email=False

            print("password aren't identicals")
            identicals=False

            return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email})
    return render(request, "accounts/infos.html", {'user':user, 'identicals':identicals,'email':email})
