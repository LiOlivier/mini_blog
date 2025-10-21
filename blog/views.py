from django.shortcuts import render
from .models import Post 

def home(request): #request = instance httpRequest
    Posts = Post.objects.all().order_by('-created_at') # récupération + tri posts décroissant
    return render(request, 'blog/home.html', {'Posts': Posts}) # post -> template -> context 