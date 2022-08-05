from django.contrib import admin
from django.urls import path
from birrap_proyecto.views import template_base
from products.views import create_product



urlpatterns = [
    path('admin/', admin.site.urls),
    path("template_base/", template_base, name='template_base'),
    path('create_products/', create_product, name='create_products'),
]
