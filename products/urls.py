from unicodedata import name
from django.urls import path
from products.views import products_list,crear_botella_500cc,lista_botella_1l,crear_botella1l,crear_lata_473cc,lista_botella_lata_473cc, buscar_birra500,buscar_birra1l,buscar_lata_473cc
from products.views import delete_birra_500cc,delete_birra_1l,delete_lata_473cc

urlpatterns = [
    path('crear_botella_500/',crear_botella_500cc, name='create_products'),
    path("products_list/", products_list, name='products_list'),
    path("lista_botella_1l/",lista_botella_1l,name="lista_botella_1l"),
    path("crear_botella1l/",crear_botella1l,name="crear_botella1l"),
    path("crear_botella_lata_473cc/",crear_lata_473cc,name="crear_botella_lata_473cc"),
    path("lista_botella_lata_473cc/",lista_botella_lata_473cc,name="lista_botella_lata_473cc"),
    path("search_product/", buscar_birra500, name='search_products'),
    path("buscar_birra1l/", buscar_birra1l, name='buscar_birra1l'),
    path("buscar_lata_473cc/", buscar_lata_473cc, name='buscar_lata_473cc'),
    path("delete_birra_500cc/<int:pk>/",delete_birra_500cc,name="delete_birra_500cc"),
    path("delete_birra_1l/<int:pk>/",delete_birra_1l,name="delete_birra_1l"),
    path("delete_lata_473cc/<int:pk>/",delete_lata_473cc,name="delete_lata_473cc")
]
