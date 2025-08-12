# stories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home = basic welcome
    path('stories/', views.story_list, name='story_list'),
    path('stories/<int:id>/', views.story_detail, name='story_detail'),
]
    # Home = basic welcome
