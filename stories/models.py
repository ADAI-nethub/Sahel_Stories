from django.contrib.auth.models import User
from django.db import models
# stories/models.py

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

        # Add these fields to Story model
category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
tags = models.ManyToManyField(Tag, blank=True)
published_at = models.DateTimeField(null=True, blank=True)

class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    community = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artisans/', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Story(models.Model):
    title = models.CharField(max_length=200)
    transcript = models.TextField()
    audio_file = models.URLField(help_text="Link to audio (e.g., SoundCloud)", blank=True)
    location = models.CharField(max_length=100)
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TreePlanting(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    planted_by = models.CharField(max_length=100, help_text="Visitor name or 'Anonymous'")
    planted_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Tree for {self.story.title} at {self.planted_at}"
    