# stories/urls_api.py
from django.urls import path
from . import views_api

urlpatterns = [
    path('pending-trees/', views_api.pending_trees, name='pending_trees'),
    path('stories/', views_api.StoryListAPI.as_view(), name='story-list-api'),
    path('stories/<int:id>/', views_api.StoryDetailAPI.as_view(), name='story-detail-api'),
]
