# 📘 sahel_api/urls.py
# This file is like the map 🗺️ of your whole Django website.
# It decides which page to show when someone visits a certain link.
# sahel_api/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def root_home(request):
    return HttpResponse("Welcome to Sahel Stories!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_home, name='root_home'),
    path('stories/', include('stories.urls')),      # website pages
    path('api/', include('stories.urls_api')),      # API endpoints
]
