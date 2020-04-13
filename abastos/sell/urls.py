from django.conf.urls import url
from . import views

app_name='sell'

urlpatterns=[
url(r'^sell-list/$', views.sell_list_view,name="sell_list"),
url(r'^publish/$', views.publish,name="publish"),
url(r'^(?P<slug>[\w-]+)/$',views.sell_details, name="sell_details"),
url(r'^delete/(?P<slug>[\w-]+)/$', views.sell_delete,name="sell_delete"),
url(r'^sell-list/by-location/$', views.sell_list_by_location, name="sell_list_by_location"),
url(r'^sell-list/by-date/$', views.sell_list_by_date, name="sell_list_by_date"),
url(r'^sell-list/by-author/$', views.sell_list_by_author, name="sell_list_by_author"),
]
