from django.contrib import admin
from django.urls import path
from birrap_proyecto.views import template_base



urlpatterns = [
    path('admin/', admin.site.urls),
    path("template_base/", template_base, name='template_base'),
]
