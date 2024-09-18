from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^products/$', list_products, name='list_products'),
    re_path(r'^products/create/$', create_product, name='create_product'),
]