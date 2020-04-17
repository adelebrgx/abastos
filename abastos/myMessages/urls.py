from django.conf.urls import url
from . import views

app_name='myMessages'

urlpatterns=[
url(r'^messages-list/$', views.messages_list_view,name="messages_list"),

]
