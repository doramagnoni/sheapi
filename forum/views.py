from rest_framework import generics, permissions
from .models import ForumTopic, ForumPost
from .serializers import ForumTopicSerializer, ForumPostSerializer

class ForumTopicList(generics.ListCreateAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
