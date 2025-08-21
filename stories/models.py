from django.db import models
from django.contrib.auth.models import User

# First, you need to define CustomUser or use User directly
# If you want a custom user, you'll need to create it properly
# For now, I'll assume you're using the default User model

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
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    transcript = models.TextField()
    audio_file = models.URLField(help_text="Link to audio (e.g., SoundCloud)", blank=True)
    location = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    
    def get_location(self):
        if self.latitude and self.longitude:
            return f"{self.latitude}, {self.longitude}"
        return self.location or "Location not available"


class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.story.title}'


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed from CustomUser to User
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField(User, related_name='attending', blank=True)

    def __str__(self):
        return self.title
    
    def available_slots(self):
        return self.capacity - self.attendees.count()


class TreePlanting(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    planted_by = models.CharField(max_length=100, help_text="Visitor name or 'Anonymous'")
    planted_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Tree for {self.story.title} by {self.planted_by}"