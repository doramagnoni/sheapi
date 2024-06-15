from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  

class ForumTopic(models.Model):  # Renamed from Topic
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']  # Latest topics first

    def __str__(self):
        return self.title

class ForumPost(models.Model):  # Renamed from Post
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  

    def __str__(self):
        return self.content[:50]  