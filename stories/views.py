# stories/views.py
from rest_framework import generics, permissions
from .models import Story
from .serializers import StorySerializer
from .permissions import IsAdminOrReadOnly  

class StoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAdminOrReadOnly]  # Custom permission for admin-only create
    
class StoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAdminOrReadOnly]  # Custom permission for admin-only update/delete
