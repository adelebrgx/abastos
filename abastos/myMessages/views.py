# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import myMessage
from django.contrib.auth.models import User
from django.http import HttpResponse


def messages_list_received_view(request):
    user=request.user
    type="received"
    messages=myMessage.objects.filter(recipient=user)
    return render(request,"myMessages/myMessageslist.html", {'messages':messages,'user':user,'type':type})

def messages_list_sent_view(request):
    user=request.user
    type="sent"
    messages=myMessage.objects.filter(author=user)
    return render(request,"myMessages/myMessageslist.html", {'user':user,'messages':messages,'type':type})

def message_details_view(request,slug):
    message=myMessage.objects.get(slug=slug)
    return render(request, "myMessages/message_detail.html", {'message':message})



def new_message_view(request):
    myuser=request.user
    users=User.objects.all()
    messages=myMessage.objects.all().order_by('date')
    if request.method=="POST":
        myHead=request.POST['head']
        myContent=request.POST['content']
        myAuthor=request.user
        myRecipient=User.objects.get(username=request.POST['recipient'])
        mySlug=str(myHead)+"-"+str(myAuthor)+"-"+str(myRecipient)
        print(myHead)
        print(myContent)
        print(myAuthor)
        print(myRecipient)
        print(mySlug)
        message=myMessage.objects.create(head=myHead, content=myContent, author=myAuthor, recipient=myRecipient, slug=mySlug)
        message.save()
        return render(request, "myMessages/myMessageslist.html", {'messages':messages, 'user':myuser})


    return render(request, "myMessages/new_message.html", {'messages':messages, 'myuser':myuser, 'users':users})
