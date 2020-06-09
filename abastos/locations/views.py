# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Location
from sell.models import SellPair
from . import forms
from django.http import HttpResponse
import re


def locations_list_view(request):
    sellpairs=SellPair.objects.all().order_by('product')
    locations=Location.objects.all().order_by('owner')
    return render(request, "locations/locationslist.html", {'locations':locations, 'sellpairs':sellpairs} )

@login_required(login_url="/accounts/login/")
def publish(request):
    isName=True
    isLat=True
    isLong=True
    sellpairs_list=SellPair.objects.all().order_by('product')
    if request.method=="POST":
        locations=Location.objects.all().order_by('owner')
        form=forms.CreateLocation(request.POST, request.FILES)
        if form.is_valid():
            name=request.POST['name']
            slug=name.replace(" ", "-")
            slug=slug+"-"+str(request.user.username)
            north=request.POST['north_coordinate']
            east=request.POST['east_coordinate']
            owner=request.user
            if(correct_name(name)==False):
                isName=False
            if(correct_lat(north)==False):
                isLat=False
            if(correct_long(east)==False):
                isLong=False
            if(isLat==True and isLong==True and isName==True):
                location=Location.objects.create(name=name, north_coordinate=north, east_coordinate=east, owner=request.user, slug=slug)
                location.save()
                return render(request, 'locations/locationslist.html', {'user':request.user, 'locations':locations, 'sellpairs':sellpairs_list})
            else:
                return render(request, 'locations/publish.html', {'form':form,'user':request.user, 'isName':isName, 'isLong':isLong, "isLat":isLat })
    else:
        form=forms.CreateLocation()
    return render(request, 'locations/publish.html', {'form':form,'user':request.user, 'isName':isName,'isLong':isLong, "isLat":isLat })

def location_details(request, slug):
    locations=Location.objects.all().order_by('owner')
    user=request.user
    sellpairs_list=SellPair.objects.all().order_by('product')
    location= Location.objects.get(slug=slug)
    isName=True
    isLat=True
    isLong=True
    print(slug)
    if request.method=='POST':
        new_name=request.POST.get("name")
        new_nc=request.POST.get("north_coordinate")
        new_ec=request.POST.get("east_coordinate")
        slug=new_name.replace(" ", "-")
        slug=slug+"-"+(str(request.user.username))
        if(correct_name(new_name)==False):
            isName=False
        if(correct_lat(new_nc)==False):
            isLat=False
        if(correct_long(new_ec)==False):
            isLong=False
        if(isLat==True and isLong==True and isName==True):
            location.name=new_name
            location.north_coordinate=new_nc
            location.east_coordinate=new_ec
            location.slug=slug
            location.save()
            return render(request, 'locations/locationslist.html', {'user':user, 'locations':locations, 'sellpairs':sellpairs_list})
        else:
            return render(request, "locations/location_details.html", {'user':user, 'location':location,'isName':isName,'isLong':isLong, "isLat":isLat})
    return render(request, "locations/location_details.html", {'user':user, 'location':location,'isName':isName,'isLong':isLong, "isLat":isLat})

def correct_name(s):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
    if(regex.search(s) == None):
        return True
    return False

def correct_lat(lat):
    result = re.match("^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$",lat)
    if (result==None):
        return False
    return True

def correct_long(long):
    result = re.match("^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$",long)
    if (result==None):
        return False
    return True

def location_delete(request,slug):
    location= Location.objects.get(slug=slug)
    sellpairs=SellPair.objects.all()

    print(location)
    for s in sellpairs:
        if s.sell.location==location:
            s.delete()
    location.delete()
    locations=Location.objects.all().order_by('owner')
    user=request.user
    sellpairs_list=SellPair.objects.all().order_by('product')
    return render(request, 'locations/locationslist.html', {'locations':locations,'user':request.user, 'sellpairs':sellpairs_list})
