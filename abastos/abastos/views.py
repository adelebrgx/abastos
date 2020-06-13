from django.http import HttpResponse
from django.shortcuts import render
from locations.models import Location
from sell.models import SellPair
from products.models import Product

def homepage(request):
    print(request.user)
    mapbox_accessToken = 'pk.eyJ1IjoiYWRlbGVib3VyZ2VpeCIsImEiOiJja2I2aXRiMmUwNnliMnNtbjFvMGVudGprIn0.aNQWYIpxou51xMciFZWVAQ'
    locations=Location.objects.all()
    sellpairs=SellPair.objects.all()
    products=Product.objects.all()

    return render(request,'homepage.html',{'user':request.user, 'token':mapbox_accessToken, 'locations':locations,'sellpairs':sellpairs, 'products':products})


def byproduct(request,slug):
    print(slug)
    mapbox_accessToken = 'pk.eyJ1IjoiYWRlbGVib3VyZ2VpeCIsImEiOiJja2I2aXRiMmUwNnliMnNtbjFvMGVudGprIn0.aNQWYIpxou51xMciFZWVAQ'
    locations=Location.objects.all()
    sellpairs=SellPair.objects.all()
    products=Product.objects.all()

    return render(request,'homepage.html',{'user':request.user, 'token':mapbox_accessToken, 'locations':locations,'sellpairs':sellpairs, 'products':products})
