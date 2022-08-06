from django.db import models

class Products(models.Model):
    name = models.CharField (max_length=50,null=True,blank=True)
    style = models.CharField (max_length=50,null=True,blank=True)
    alcohol_volume = models.FloatField (max_length=2,null=True,blank=True)
    IBU = models.FloatField (max_length=2,null=True,blank=True)
    description = models.CharField (max_length=2500,null=True,blank=True)
    malt = models.CharField (max_length=50,null=True,blank=True)
    hop = models.CharField (max_length=50,null=True,blank=True)
    price = models.FloatField (default=True, null=True,blank=True)
    creation_date = models.DateField (auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField (default=True)

class Category(models.Model):
    name = models.CharField (max_length=255)