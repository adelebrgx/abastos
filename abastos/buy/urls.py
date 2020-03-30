from django.conf.urls import url
from . import views

app_name='buy'

urlpatterns=[
url(r'^buy-list/$', views.buy_list_view,name="buy_list")
]
