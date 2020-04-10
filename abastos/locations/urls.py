from django.conf.urls import url
from . import views

app_name='locations'

urlpatterns=[
url(r'^locations-list/$', views.locations_list_view,name="locations_list"),
url(r'^publish/$', views.publish, name="publish"),
url(r'^(?P<slug>[\w-]+)/$',views.location_details, name="location_details"),
url(r'^delete/(?P<slug>[\w-]+)/$', views.location_delete,name="location_delete"),
]
