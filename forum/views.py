from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ForumTopic, ForumPost
from .serializers import ForumTopicSerializer, ForumPostSerializer

class ForumTopicList(generics.ListCreateAPIView):
    serializer_class = ForumTopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ForumTopic.objects.annotate(
        posts_count=Count('posts', distinct=True),
    ).order_by('-updated_at')

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
        'posts_count',
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



class ForumTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ForumPostList(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ForumPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
