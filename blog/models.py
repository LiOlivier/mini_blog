from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) #Titre du post
    content = models.TextField() #Contenue du post
    created_at = models.DateTimeField(default=timezone.now) #Quand le post à été publier 
    author = models.ForeignKey( 'auth.User', on_delete=models.CASCADE) # auteur du post

    def __str__(self):
        return self.title 