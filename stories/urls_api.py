# stories/urls_api.py
from django.urls import path
from . import views_api

urlpatterns = [
    # Story endpoints
    path("stories/", views_api.StoryListAPI.as_view(), name="story-list-api"),
    path("stories/<int:id>/", views_api.StoryDetailAPI.as_view(), name="story-detail-api"),
    path("stories/create/", views_api.StoryCreateAPI.as_view(), name="story-create-api"),
    
    # Event endpoints
    path("events/", views_api.EventListAPI.as_view(), name="event-list-api"),
    
    # Utility endpoints
    path("health/", views_api.health_check, name="health-check"),
    path("test/", views_api.ping, name="test-api"),
    path("user/", views_api.current_user, name="current-user"),
]