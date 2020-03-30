from django.conf.urls import url
from . import views

app_name='sell'

urlpatterns=[
url(r'^sell-list/$', views.sell_list_view,name="sell_list")
]
