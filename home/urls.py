from django.urls import path
from .views import *


app_name = 'home'


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('products/<str:category>', products, name='products_with_category'),
    path('product-informations/<int:pid>', product , name='product_info'),
    path('create-product', create_product , name='create_product'),
    path('search-product/', product , name='products_with_search'),
]
