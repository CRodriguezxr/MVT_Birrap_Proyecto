from django.urls import path
from home.views import create_article

urlpatterns = [
    path('create_article/', create_article, name='create_article'),
]
