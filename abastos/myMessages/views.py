# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def messages_list_view(request):
    return render(request,"myMessages/myMessageslist.html")
