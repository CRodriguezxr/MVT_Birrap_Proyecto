from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=10000,null=True,blank=True)
    description_2 = models.CharField(max_length=10000,null=True,blank=True)
    team = models.CharField(max_length=2000,null=True,blank=True)
    author = models.CharField(max_length=2000,null=True,blank=True)
