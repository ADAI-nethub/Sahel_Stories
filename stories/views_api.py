# 📦 Import tools to build APIs
from rest_framework import generics  # For common API patterns (list, create, detail)
from rest_framework.decorators import api_view  # To make simple API functions
from rest_framework.response import Response  # To send info back to the user
from rest_framework.authentication import SessionAuthentication  # Checks if user is logged in
from rest_framework.permissions import IsAuthenticated  # Only allow logged-in users
from rest_framework.exceptions import ValidationError  # Shows clear error messages

# 📬 Other Django tools
from django.http import JsonResponse  # For quick yes/no responses
from django.utils import timezone  # To get current time ⏰
from django.contrib.auth.models import User  # Built-in user system

# 🧱 Our blueprints (models) for data
from .models import Story, Event, TreePlanting

# 🔧 Tools that turn models into JSON and back
from .serializers import StorySerializer, EventSerializer


# ------------------------------------------------------------------------------
# 🌱 Tree Planting API
# ------------------------------------------------------------------------------

@api_view(['GET'])
def pending_trees(request):
    """
    📋 Show all trees that are promised but not yet planted.
    Like a to-do list of trees waiting to go into the ground 🌳.
    """
    pending = TreePlanting.objects.filter(status='pending')

    data = []
    for tree in pending:
        data.append({
            "id": tree.id,
            "story_title": tree.story.title,
            "planted_by": tree.planted_by,
            "promised_at": tree.planted_at,
            "story_url": f"https://yourapp.com/stories/{tree.story.id}/"
        })

    return Response(data)


# ------------------------------------------------------------------------------
# 🔧 Health & Utility Endpoints
# ------------------------------------------------------------------------------

@api_view(['GET'])
def ping(request):
    """Test if server is awake. Like saying ‘ping’ and hearing ‘pong’ 🏓."""
    return JsonResponse({"message": "pong"})


@api_view(['GET'])
def health_check(request):
    """Check if API is healthy. Like asking a robot, ‘How are you?’ 🤖."""
    return JsonResponse({
        "status": "ok",
        "timestamp": timezone.now().isoformat(),
        "service": "Sahel Stories API"
    })


@api_view(['GET'])
def current_user(request):
    """
    Show who is logged in right now 👤.
    If nobody is logged in, say “Not authenticated.”
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Not authenticated"}, status=401)

    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "is_authenticated": True
    })


# ------------------------------------------------------------------------------
# 📚 Story API Views
# ------------------------------------------------------------------------------

class StoryListAPI(generics.ListAPIView):
    """📖 Show all published stories. Like a bookshelf of finished books 📚."""
    queryset = Story.objects.filter(published_at__isnull=False)
    serializer_class = StorySerializer


class StoryDetailAPI(generics.RetrieveAPIView):
    """🔍 Show details of one story. Like pulling one book off the shelf."""
    queryset = Story.objects.filter(published_at__isnull=False)
    serializer_class = StorySerializer
    lookup_field = "id"  # find by story ID


class StoryCreateAPI(generics.CreateAPIView):
    """✍️ Let a logged-in artisan write a new story (like giving them a notebook)."""
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            artisan = self.request.user.artisan  # link story to storyteller
            serializer.save(artisan=artisan)
        except AttributeError:
            raise ValidationError(
                "User does not have an artisan profile. Please complete your profile first."
            )


# ------------------------------------------------------------------------------
# 📅 Event API Views
# ------------------------------------------------------------------------------

class EventListAPI(generics.ListAPIView):
    """🗓️ Show all upcoming events. Like a calendar of fun stuff 🎉."""
    queryset = Event.objects.filter(date_time__gte=timezone.now()).order_by("date_time")
    serializer_class = EventSerializer


class EventDetailAPI(generics.RetrieveAPIView):
    """📨 Show details for one event. Like reading the invite to a party 🎈."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"


# ------------------------------------------------------------------------------
# ✅ END OF FILE
# ------------------------------------------------------------------------------
