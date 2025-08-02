# stories/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Story

def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})

def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    return render(request, 'stories/story_detail.html', {'story': story})