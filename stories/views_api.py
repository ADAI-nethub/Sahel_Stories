# 📦 Import tools to build APIs
from rest_framework import generics  # For common API patterns like list, create, retrieve
from rest_framework.decorators import api_view  # To create simple functions for APIs
from rest_framework.response import Response  # To send info back to users
from rest_framework.authentication import SessionAuthentication  # Checks login session
from rest_framework.permissions import IsAuthenticated  # Allows only logged-in users

# 🧰 Error handling (important fix!)
from rest_framework.exceptions import ValidationError  # To show errors clearly

# 📬 Other Django tools
from django.http import JsonResponse  # Sends simple responses (like "pong")
from django.utils import timezone  # Deals with current date and time
from django.contrib.auth.models import User  # Built-in user system

# 🧱 Our models (like blueprints for data)
from .models import Story, Event

# 🔧 Tools to turn models into JSON and back
from .serializers import StorySerializer, EventSerializer


# ------------------------------------------------------------------------------
# 🔧 Health & Utility Endpoints
# ------------------------------------------------------------------------------

@api_view(['GET'])
def ping(request):
    """
    Test if server is alive. Like saying "Are you awake?" and hearing "pong!".
    """
    return JsonResponse({"message": "pong"})


@api_view(['GET'])
def health_check(request):
    """
    Says that the API is running well and shows the current time.
    Like checking a robot’s battery and clock.
    """
    return JsonResponse({
        "status": "ok",
        "timestamp": timezone.now().isoformat(),
        "service": "Sahel Stories API"
    })


@api_view(['GET'])
def current_user(request):
    """
    Shows who is currently logged in. If no one, sends an error.
    Like asking “Who’s using this phone right now?”
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
    """
    Shows all stories that have been published.
    Like a bookshelf of finished books.
    """
    queryset = Story.objects.filter(published_at__isnull=False)  # Only published stories
    serializer_class = StorySerializer  # Automatically uses read-only version under the hood


class StoryDetailAPI(generics.RetrieveAPIView):
    """
    Shows details about one specific story (if it's published).
    Like picking one book to read from the shelf.
    """
    queryset = Story.objects.filter(published_at__isnull=False)
    serializer_class = StorySerializer
    lookup_field = 'id'  # Look up stories using their unique ID


class StoryCreateAPI(generics.CreateAPIView):
    """
    Lets a logged-in user (storyteller) create a new story.
    Like giving a notebook to a writer.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            # Connect the story to the storyteller (Artisan)
            artisan = self.request.user.artisan
            serializer.save(artisan=artisan)
        except AttributeError:
            # If the user doesn’t have an artisan profile yet, show an error
            raise ValidationError(
                "User does not have an artisan profile. Please complete your profile first."
            )


# ------------------------------------------------------------------------------
# 📅 Event API Views
# ------------------------------------------------------------------------------

class EventListAPI(generics.ListAPIView):
    """
    Shows all upcoming events. Like a calendar of cool stuff coming up.
    """
    queryset = Event.objects.filter(date_time__gte=timezone.now()).order_by('date_time')
    serializer_class = EventSerializer


class EventDetailAPI(generics.RetrieveAPIView):
    """
    Shows details about one event.
    Like reading the invite to a specific party.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'

# ------------------------------------------------------------------------------
# ✅ END OF FILE
# ------------------------------------------------------------------------------
