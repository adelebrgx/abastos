from django.conf.urls import url
from . import views

app_name='locations'

urlpatterns=[
url(r'^locations-list/$', views.locations_list_view,name="locations_list")
]
