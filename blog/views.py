from django.shortcuts import render
from .models import Post
from django.http import Http404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

#(contexte pluriel)
@login_required
def home(request): #request = instance httpRequest
    posts = Post.objects.all().order_by('-created_at') # récupération + tri posts décroissant
    return render(request, 'blog/home.html', {'posts': posts}) # posts -> template -> context

#(contexte singulier)
def post_detail(request, post_id): # détail + id du post
    post = Post.objects.get(id=post_id) # identification du post <=> id 
    return render(request, 'blog/post_detail.html', {'post': post}) # post detail -> template -> context

@login_required
def create_form(request):
    if request.method == 'POST': # form soumis 
        form = PostForm(request.POST) # données du form récupérées
        if form.is_valid(): 
            obj = form.save(commit=False)
            if hasattr(obj, 'author') and request.user.is_authenticated:
                obj.author = request.user
            obj.save()
            return redirect('home') # redirection vers la page d'accueil après sauvegarde
    else:
        form = PostForm() # soumission vide 
    return render(request, 'blog/create_form.html', {'form': form}) # form vide -> template -> context

def login_view(request):
    return render(request, 'registration/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})