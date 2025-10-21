# le projet Django renvoie la main au urls.py de l'app blog, car il possède un path /...

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
]