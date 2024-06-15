from rest_framework import serializers
from .models import ForumTopic, ForumPost

class ForumPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = ForumPost
        fields = ['id', 'topic', 'author', 'content', 'created_at', 'updated_at']

class ForumTopicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    posts = ForumPostSerializer(many=True, read_only=True) 

    class Meta:
        model = ForumTopic
        fields = ['id', 'title', 'author', 'created_at', 'updated_at', 'posts']