from django.contrib import admin
from products.models import Products,Botella_1l,Botella_lata_473cc

# Register your models here.



@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display= ["name","price","is_active"]

@admin.register(Botella_1l)
class Products_admin(admin.ModelAdmin):
    list_display= ["name","price","is_active"]

@admin.register(Botella_lata_473cc)
class Products_admin(admin.ModelAdmin):
    list_display= ["name","price","is_active"]