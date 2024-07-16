from django.urls import path
from .views import StoryListCreateAPIView, StoryRetrieveUpdateDestroyAPIView

urlpatterns = [
     path('stories/', StoryListCreateAPIView.as_view(), name='story-list-create'),
     path('stories/<int:pk>/', StoryRetrieveUpdateDestroyAPIView.as_view(), name='story-retrieve-update-delete'),
]