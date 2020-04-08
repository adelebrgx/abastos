# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Location
from sell.models import SellPair
from . import forms
from django.http import HttpResponse


def locations_list_view(request):
    sellpairs=SellPair.objects.all().order_by('product')
    locations=Location.objects.all().order_by('owner')
    return render(request, "locations/locationslist.html", {'locations':locations, 'sellpairs':sellpairs} )

def publish(request):
    if request.method=="POST":
        locations=Location.objects.all().order_by('owner')
        form=forms.CreateLocation(request.POST, request.FILES)
        if form.is_valid():
            name=request.POST['name']
            slug=name.replace(" ", "-")
            print(slug)
            north=request.POST['north_coordinate']
            east=request.POST['east_coordinate']
            print(name)
            print(north)
            print(east)
            owner=request.user
            location=Location.objects.create(name=name, north_coordinate=north, east_coordinate=east, owner=owner)
            location.save()

            return render(request, 'locations/locationslist.html', {'locations':locations,'user':request.user})
    else:
        form=forms.CreateLocation()
    return render(request, 'locations/publish.html', {'form':form,'user':request.user})

def location_details(request, slug):
    locations=Location.objects.all().order_by('owner')
    user=request.user
    location= Location.objects.get(slug=slug)
    print(location)
    if request.method=='POST':
        new_name=request.POST.get("name")
        new_nc=request.POST.get("north_coordinate")
        new_ec=request.POST.get("east_coordinate")
        location.name=new_name
        location.north_coordinate=new_nc
        location.east_coordinate=new_ec
        location.save()
        return render(request, 'locations/locationslist.html', {'user':user, 'locations':locations})
    return render(request, "locations/location_details.html", {'user':user, 'location':location})
