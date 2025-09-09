# 📘 stories/views.py
"""
Views for the Stories app.

Handles:
- Story listing and details
- Tree planting actions
- Map visualization
- View tracking
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Story, TreePlanting
from .google_sheets import get_google_sheet
from .services.treeplanting import mark_tree_planted
import json


# ==============================
# Public Story Views
# ==============================

def home(request):
    """Render the home page."""
    return render(request, 'stories/home.html')


def story_list(request):
    """Display a list of all stories."""
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})


def story_detail(request, id):
    """
    Display a single story and increment its view count.
    """
    story = get_object_or_404(Story, id=id)
    
    # Increment view count
    story.views += 1
    story.save(update_fields=['views'])  # Efficient save

    return render(request, 'stories/story_detail.html', {'story': story})


# ==============================
# Tree Planting Action
# ==============================

@require_http_methods(["POST"])
def plant_tree(request, id):
    """
    Handle a tree planting action for a given story.
    Accepts POST only.
    """
    story = get_object_or_404(Story, id=id)
    visitor_name = request.user.username if request.user.is_authenticated else "Guest"

    # Create the tree planting record
    tree = TreePlanting.objects.create(
        story=story,
        planted_by=visitor_name,
        status=TreePlanting.Status.PENDING,
    )

    # Try to sync to Google Sheets
    try:
        sheet = get_google_sheet()
        sheet.append_row([
            tree.id,
            story.title,
            visitor_name,
            tree.status,
            timezone.now().isoformat(),
        ])
    except Exception as e:
        messages.warning(
            request,
            f"Your tree was recorded, but we couldn't sync to our main log: {e}"
        )

    return redirect('story_detail', id=story.id)


# ==============================
# Map View (GeoJSON)
# ==============================

def story_map(request):
    """
    Display a map with all stories that have tree plantings and valid coordinates.
    Returns GeoJSON for frontend mapping libraries (e.g., Leaflet).
    """
    stories = Story.objects.filter(
        tree_plantings__isnull=False,
        latitude__isnull=False,
        longitude__isnull=False
    ).distinct()

    stories_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [story.longitude, story.latitude]
                },
                "properties": {
                    "title": story.title,
                    "location": story.location,
                    "tree_count": story.tree_plantings.count(),
                    "url": request.build_absolute_uri(story.get_absolute_url())
                }
            }
            for story in stories
        ]
    }

    return render(request, 'stories/story_map.html', {
        'stories_geojson': json.dumps(stories_geojson, indent=2)
    })


# ==============================
# Optional: Scraping Endpoint (Remove if not used)
# ==============================

# Only keep this if you really need it.
# Otherwise, delete it to reduce attack surface and complexity.

# from .selenium_scraper import get_page_content
#
# @login_required  # Protect this
# def scrape_view(request):
#     """
#     Example view for scraping (debug only). Remove in production.
#     """
#     url = "https://example.com"
#     try:
#         content = get_page_content(url)
#         return JsonResponse({"content_length": len(content)})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)