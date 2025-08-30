# stories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('map/', views.story_map, name='story_map'),
    path('<int:id>/', views.story_detail, name='story_detail'),
    path('home/', views.home, name='home'),
]
#AttributeError: module 'stories.views' has no attribute 'story_detail'