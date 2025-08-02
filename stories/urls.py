# stories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<int:id>/', views.story_detail, name='story_detail'),
]