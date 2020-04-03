from django.conf.urls import url
from . import views

app_name='products'

urlpatterns=[
url(r'^products-list/$', views.products_list_view,name="products_list")
]
