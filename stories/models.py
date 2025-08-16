from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    community = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artisans/', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Story(models.Model):
    title = models.CharField(max_length=255)
    artisan = models.ForeignKey('Artisan', on_delete=models.CASCADE)
    transcript = models.TextField()
    audio_file = models.URLField(help_text="Link to audio (e.g., SoundCloud)", blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)  # ✅ publication date
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)  # ← Must exist

    def __str__(self):
        return f'Comment by {self.name}'


class TreePlanting(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    planted_by = models.CharField(max_length=100, help_text="Visitor name or 'Anonymous'")
    planted_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Tree for {self.story.title} at {self.planted_at}"
