from unicodedata import name
from django.urls import path
from products.views import products_list,crear_botella_500cc,lista_botella_1l,crear_botella1l,crear_lata_473cc,lista_botella_lata_473cc, buscar_birra500

urlpatterns = [
    path('crear_botella_500/',crear_botella_500cc, name='create_products'),
    path("products_list/", products_list, name='products_list'),
    path("lista_botella_1l/",lista_botella_1l,name="lista_botella_1l"),
    path("crear_botella1l/",crear_botella1l,name="crear_botella1l"),
    path("crear_botella_lata_473cc/",crear_lata_473cc,name="crear_botella_lata_473cc"),
    path("lista_botella_lata_473cc/",lista_botella_lata_473cc,name="lista_botella_lata_473cc"),
    path("search_product/", buscar_birra500, name='search_products')
]
