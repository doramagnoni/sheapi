from rest_framework import generics, permissions, filters
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import Story
from .serializers import StorySerializer
from rest_framework.permissions import BasePermission, IsAdminUser



class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAdminOrReadOnly]
    

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


    def get_serializer_context(self):
        return {'request': self.request}


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAdminOrReadOnly]


    def perform_update(self, serializer):
       
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            
            raise PermissionDenied("You must be logged in to update this story.")