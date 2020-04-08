from django.conf.urls import url
from . import views

app_name='sell'

urlpatterns=[
url(r'^sell-list/$', views.sell_list_view,name="sell_list"),
url(r'^publish/$', views.publish,name="publish"),
url(r'^(?P<slug>[\w-]+)/$',views.sell_details, name="sell_details"),
]
