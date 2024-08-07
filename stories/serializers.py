from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Story model.
    """
    class Meta:
        model = Story
        fields = '__all__'
