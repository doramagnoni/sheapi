from django.db import models
from django.contrib.auth.models import User  

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    image = models.ImageField(upload_to='images/', default='../two-ladies_iqfqjr', blank=True, null=True)
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title