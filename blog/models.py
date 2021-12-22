from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=100)
    teaser = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='General')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='comments')
    
    class Meta:
        ordering = ['date_posted']
    
    def __str__(self):
        return self.body
    
    


