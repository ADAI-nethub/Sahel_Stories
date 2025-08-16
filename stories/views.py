from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Story
from .serializers import StorySerializer


class StoryCreateAPI(generics.CreateAPIView):
    """
    API endpoint to create a new Story.
    Requires authentication, links the created story to the logged-in artisan.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        artisan = self.request.user.artisan  # assumes a OneToOne link User → Artisan
        serializer.save(artisan=artisan)


def home(request):
    return HttpResponse("Welcome to Sahel Stories!")


def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})


def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    return render(request, 'stories/story_detail.html', {'story': story})
