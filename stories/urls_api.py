# stories/urls_api.py
from django.urls import path
from . import views_api

urlpatterns = [
    path("stories/", views_api.StoryListAPI.as_view(), name="story-list-api"),
    path("stories/<int:id>/", views_api.StoryDetailAPI.as_view(), name="story-detail-api"),
]
