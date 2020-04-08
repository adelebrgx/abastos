from django.conf.urls import url
from . import views

app_name='products'

urlpatterns=[
url(r'^products-list/$', views.products_list_view,name="products_list"),
url(r'^publish/$', views.publish,name="products_list"),
url(r'^(?P<slug>[\w-]+)/$',views.product_details, name="product_details"),
#url(r'^delete/$', views.product_delete,name="product_delete"),
]
