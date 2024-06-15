from django.urls import path, include
from .views import ForumTopicList, ForumTopicDetail, ForumPostList, ForumPostDetail

urlpatterns = [
    path('forum/topics/', ForumTopicList.as_view(), name='forum-topic-list'),
    path('forum/topics/<int:pk>/', ForumTopicDetail.as_view(), name='forum-topic-detail'),
    path('forum/topics/<int:topic_pk>/posts/', ForumPostList.as_view(), name='forum-post-list'),  
    path('forum/posts/<int:pk>/', ForumPostDetail.as_view(), name='forum-post-detail'),
]