# stories/urls.py
from django.urls import path, include 
from . import views  # for normal HTML views like home, story_list, story_detail
from . import views_api  # for DRF API views



urlpatterns = [
    path('', include('stories.urls')),
    path('api/events/', views_api.EventListAPI.as_view(), name='event-list-api'),
    # stories/urls.py
    path('map/', views.story_map, name='story_map'),
    # API endpoints
    path("api/stories/", views_api.StoryListAPI.as_view(), name="story-list-api"),
    path("api/stories/<int:id>/", views_api.StoryDetailAPI.as_view(), name="story-detail-api"),

    # Regular Django views
    path("", views.home, name="home"),
    path("stories/", views.story_list, name="story_list"),
    path("stories/<int:id>/", views.story_detail, name="story_detail"),

    path('stories/create/', views_api.StoryCreateAPI.as_view(), name='story-create-api'),
]
