# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Location


def locations_list_view(request):
    locations=Location.objects.all().order_by('owner')
    return render(request, "locations/locationslist.html", {'locations':locations} )
