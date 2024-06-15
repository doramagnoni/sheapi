from django.urls import path
from .views import StoryList, StoryDetail

urlpatterns = [
    path('stories/', StoryList.as_view(), name='story-list'),
    path('stories/<int:pk>/', StoryDetail.as_view(), name='story-detail'),
]