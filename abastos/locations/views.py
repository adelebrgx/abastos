# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Location
from . import forms


def locations_list_view(request):
    locations=Location.objects.all().order_by('owner')
    return render(request, "locations/locationslist.html", {'locations':locations} )

def publish(request):
    if request.method=="POST":
        locations=Location.objects.all().order_by('owner')
        form=forms.CreateLocation(request.POST, request.FILES)
        if form.is_valid():
            name=request.POST['name']
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
