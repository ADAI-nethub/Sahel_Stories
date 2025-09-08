"""
Root URL Configuration for Sahel_Stories

This module defines the main URL routes for the project.
It includes:
- Admin interface
- Homepage
- App-specific URL patterns (stories, API)
- Static & media file serving in development
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# 🏠 Homepage view
def home(request):
    """
    Simple welcome view for the root URL.
    Replace with a proper template view in production.
    """
    return HttpResponse("<h1>Welcome to Sahel Stories!</h1><p>Planting trees, one story at a time. 🌳</p>")


# 🗺️ URL patterns
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Web pages
    path('', home, name='home'),
    path('stories/', include('stories.urls')),       # Story pages (e.g., /stories/, /stories/5/)

    # API endpoints
    path('api/', include('stories.urls_api')),       # REST API (e.g., /api/stories/, /api/plant/)
]

# 🔧 Serve static and media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)