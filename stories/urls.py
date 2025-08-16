# stories/urls.py
from django.urls import path
from . import views
from .views import StoryListAPI, StoryDetailAPI

urlpatterns = [
    # HTML views
    path("", views.home, name="home"),  
    path("stories/", views.story_list, name="story_list"),
    path("stories/<int:id>/", views.story_detail, name="story_detail"),

    # API views
    path("api/stories/", StoryListAPI.as_view(), name="story-list"),
    path("api/stories/<int:id>/", StoryDetailAPI.as_view(), name="story-detail"),
]
