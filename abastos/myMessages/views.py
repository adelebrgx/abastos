# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import myMessage
from django.contrib.auth.models import User
from django.http import HttpResponse


def messages_list_received_view(request):
    user=request.user
    type="received"
    messages=myMessage.objects.filter(recipient=user).order_by('-date')
    return render(request,"myMessages/myMessageslist.html", {'messages':messages,'user':user,'type':type})

def messages_list_sent_view(request):
    user=request.user
    type="sent"
    messages=myMessage.objects.filter(author=user).order_by('-date')
    return render(request,"myMessages/myMessageslist.html", {'user':user,'messages':messages,'type':type})

def message_details_view(request,slug):
    if request.method=="POST":
        messages=myMessage.objects.all()
        myuser=request.user
        type="received"
        myContent=request.POST.get('content')
        Head=request.POST.get('head')
        myHead=" ".join(Head.split("-"))
        myHead="Re:"+myHead
        myId=request.POST.get('conv_id')
        recipient=request.POST.get('original_author')
        mySlug="none"
        print(mySlug)
        myAuthor=request.user
        print(myAuthor)
        print(myContent)
        print(myHead)
        print(myId)
        myRecipient=User.objects.get(username=recipient)
        print(myRecipient)
        message=myMessage.objects.create(conv_id=myId, head=myHead, content=myContent, author=myAuthor, recipient=myRecipient, slug=mySlug)
        message.slug=str(Head)+"-"+str(myAuthor)+"-"+str(myRecipient)+"-"+str(message.id)
        message.save()
        mymessages=myMessage.objects.filter(recipient=myuser)
        return render(request, "myMessages/myMessageslist.html", {'messages':mymessages, 'user':myuser, 'type':type})

    message=myMessage.objects.get(slug=slug)
    conv_id=message.conv_id
    messages=myMessage.objects.filter(conv_id=conv_id)
    print(messages)
    return render(request, "myMessages/message_detail.html", {'message':message, 'messages':messages})



def new_message_view(request):
    myuser=request.user
    users=User.objects.all()
    messages=myMessage.objects.filter(recipient=myuser)
    if request.method=="POST":
        myHead=request.POST['head']
        myHeadSlug="-".join( myHead.split() )
        print(myHead)
        myContent=request.POST['content']
        myAuthor=request.user
        myRecipient=User.objects.get(username=request.POST['recipient'])
        mySlug="none"
        print(myHead)
        print(myContent)
        print(myAuthor)
        print(myRecipient)
        print(mySlug)
        message=myMessage.objects.create(head=myHead, content=myContent, author=myAuthor, recipient=myRecipient, slug=mySlug)
        message.conv_id=message.id
        message.slug=str(myHeadSlug)+"-"+str(myAuthor)+"-"+str(myRecipient)+"-"+str(message.id)
        message.save()
        type="received"
        mymessages=myMessage.objects.filter(recipient=myuser)
        return render(request, "myMessages/myMessageslist.html", {'messages':mymessages, 'user':myuser, 'type':type})


    return render(request, "myMessages/new_message.html", {'messages':messages, 'myuser':myuser, 'users':users})
