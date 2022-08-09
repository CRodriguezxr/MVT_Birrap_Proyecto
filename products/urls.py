from django.urls import path
from products.views import products_list, create_product,create_1l

urlpatterns = [
    path('create_products/', create_product, name='create_products'),
    path("products_list/", products_list, name='products_list'),
    path("botella1l/",create_1l,name="botella1l")
]
