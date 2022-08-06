from django.contrib import admin
from django.urls import path, include
from birrap_proyecto.views import template_base
from products.views import create_product, products_list



urlpatterns = [
    path('admin/', admin.site.urls),
    path("template_base/", template_base, name='template_base'),
    path("products/", include("products.urls"))
]
