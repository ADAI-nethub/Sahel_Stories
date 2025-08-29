# 📘 stories/views.py

# 📘 stories/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib import messages

from .models import Story, TreePlanting
from .google_sheets import get_google_sheet
from .services.treeplanting import mark_tree_planted
import json
def story_map(request):
    """
    Display a map with all stories that have tree plantings.
    """
    stories = Story.objects.filter(
        tree_plantings__isnull=False,
        latitude__isnull=False,
        longitude__isnull=False
    ).distinct()
    
    # Convert to GeoJSON format for mapping
    stories_data = []
    for story in stories:
        stories_data.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [story.longitude, story.latitude]
            },
            'properties': {
                'title': story.title,
                'location': story.location,
                'tree_count': story.tree_plantings.count()
            }
        })
    
    return render(request, 'stories/story_map.html', {
        'stories': stories,
        'stories_geojson': json.dumps(stories_data)
    })

def story_map(request):
    """
    Display a map with all stories that have tree plantings.
    """
    stories = Story.objects.filter(tree_plantings__isnull=False).distinct()
    return render(request, 'stories/story_map.html', {'stories': stories})

def story_list(request):
    """
    Display a list of all stories.
    """
    stories = Story.objects.all()
    return render(request, 'stories/story_list.html', {'stories': stories})

def plant_tree(request, id):
    """
    Handle when a user wants to 'plant a tree' for a given Story.
    Steps:
        1️⃣ Find the story (404 if not found).
        2️⃣ Determine who is planting (user or guest).
        3️⃣ Save the tree planting promise in the database.
        4️⃣ Log the same info in Google Sheets (if available).
        5️⃣ Redirect the user to a 'success' page.
    """
    story = get_object_or_404(Story, id=id)
    visitor_name = request.user.username if request.user.is_authenticated else "Guest"
    tree = TreePlanting.objects.create(
        story=story,
        planted_by=visitor_name,
        status=TreePlanting.Status.PENDING,
    )
    try:
        sheet = get_google_sheet()
        sheet.append_row([
            tree.id,
            story.title,
            visitor_name,
            tree.status,
            str(timezone.now())
        ])
    except Exception as e:
        messages.warning(request, f"Tree saved locally but not synced to Google Sheets: {e}")
    return redirect('success')

def update_story_views(request, id):
    """
    Increment the view count for a story when accessed.
    """
    story = get_object_or_404(Story, id=id)
    story.views += 1
    story.save(update_fields=['views'])
    return redirect('story_detail', id=story.id)

    