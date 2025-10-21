from django.shortcuts import render
from .models import Post
from django.http import Http404
from .forms import PostForm
from django.shortcuts import redirect

#(contexte pluriel)
def home(request): #request = instance httpRequest
    posts = Post.objects.all().order_by('-created_at') # récupération + tri posts décroissant
    return render(request, 'blog/home.html', {'posts': posts}) # posts -> template -> context

#(contexte singulier)
def post_detail(request, post_id): # détail + id du post
    post = Post.objects.get(id=post_id) # identification du post <=> id 
    return render(request, 'blog/post_detail.html', {'post': post}) # post detail -> template -> context

def create_form(request, form_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PostForm()
    return render(request, 'blog/create_form.html', {'form': form})
