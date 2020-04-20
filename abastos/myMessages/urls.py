from django.conf.urls import url
from . import views

app_name='myMessages'

urlpatterns=[
url(r'^messages-list/$', views.messages_list_view,name="messages_list"),
url(r'^new-message/$', views.new_message_view,name="new_message"),
url(r'^(?P<slug>[\w-]+)/$',views.message_details_view, name="message_details"),

]
