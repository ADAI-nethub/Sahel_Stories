# stories/urls_api.py
from django.urls import path
from . import views_api
from django.http import JsonResponse


def ping(request):
    return JsonResponse({"message": "pong"})


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("stories/", views_api.StoryListAPI.as_view(), name="story-list-api"),
    path("stories/<int:id>/", views_api.StoryDetailAPI.as_view(), name="story-detail-api"),
    path("stories/create/", views_api.StoryCreateAPI.as_view(), name="story-create-api"),  # ✅ create API
    path("health/", health_check, name="health-check"),
    path("test/", ping, name="test-api"),
    path("user/", views_api.current_user, name="current-user"),
]
