from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Story
from .serializers import StorySerializer

class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'title',
        'author__username',
    ]
    ordering_fields = [
        'created_at',
        'updated_at',
    ]
    filterset_fields = {
        'title': ['icontains'],
        'author': ['exact'],
        'created_at': ['gte', 'lte'],
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]