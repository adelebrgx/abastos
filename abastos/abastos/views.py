from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    print(request.user)
    return render(request,'homepage.html',{'user':request.user})
