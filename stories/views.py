from rest_framework import generics, permissions
from .models import Story
from .serializers import StorySerializer

class StoryList(generics.ListCreateAPIView):
    """
    List all stories or create a new story if authenticated.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
