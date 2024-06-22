from rest_framework import serializers
from likes.serializers import LikeSerializer
from comments.serializers import CommentSerializer
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'likes', 'comments']



    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
