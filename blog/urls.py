# le projet Django renvoie la main au urls.py de l'app blog, car il possède un path /...

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_form, name='create_form'),
    path('login/', views.login_view, name='login'),
]