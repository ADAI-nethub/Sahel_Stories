from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# This class adds a timestamp (a date and time) automatically when something is created.
# Think of it like writing the date on a drawing when you finish it.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # sets the date/time when created

    class Meta:
        abstract = True  # This means this class is just a helper; no table in the database for it

# This is like a box where you put story categories, like "Adventure" or "History".
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Each category has a unique name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name  # When you print a Category, you see its name

# This holds tags, which are little labels you can put on stories to describe them, like "fun" or "sad".
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Tags also have unique names

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

# This represents an Artisan — a person who tells stories.
class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Linked user account")
    bio = models.TextField(help_text="Biography or background of the artisan")
    community = models.CharField(max_length=100, help_text="Community or local group")
    photo = models.ImageField(upload_to='artisans/', null=True, blank=True, help_text="Optional profile photo")

    def __str__(self):
        # Show the artisan's full name if available, otherwise their username
        return self.user.get_full_name() or self.user.username

# This is the main Story class where the story's details are stored.
class Story(TimeStampedModel):
    title = models.CharField(max_length=255)  # The story's title
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='stories')
    transcript = models.TextField()  # The full written story
    audio_file = models.URLField(help_text="Link to audio (e.g., SoundCloud)", blank=True)  # Optional audio URL
    location = models.CharField(max_length=100)  # Where the story took place
    latitude = models.FloatField(null=True, blank=True)  # Optional GPS latitude
    longitude = models.FloatField(null=True, blank=True)  # Optional GPS longitude

    # This is the key change that fixes the bug:
    # Instead of having a real database field called is_published, we have published_at date/time.
    # If published_at has a value, the story is published.
    published_at = models.DateTimeField(null=True, blank=True, db_index=True)

    # Category of story, can be empty, and if category is deleted, story keeps existing.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='stories')

    # Many tags can belong to one story, like stickers on a notebook.
    tags = models.ManyToManyField(Tag, blank=True, related_name='stories')

    @property
    def is_published(self):
        # This is a "property" — not saved in the database.
        # It checks if published_at has a value, meaning the story is published.
        return self.published_at is not None

    def __str__(self):
        return self.title

    def get_location(self):
        # Returns GPS coordinates if they exist, else returns location name,
        # else returns a message that location is not available.
        if self.latitude and self.longitude:
            return f"{self.latitude}, {self.longitude}"
        return self.location or "Location not available"

# This class represents comments made by readers on stories.
class Comment(TimeStampedModel):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)  # Name of commenter
    email = models.EmailField(blank=True)  # Optional email address
    body = models.TextField()  # The actual comment text
    active = models.BooleanField(default=True)  # Used to hide inappropriate comments

    def __str__(self):
        return f'Comment by {self.name} on {self.story.title}'

# This class is for events related to storytelling.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField(User, related_name='attending', blank=True)

    def __str__(self):
        return self.title

    def available_slots(self):
        # Shows how many spaces are left for people to join the event
        return self.capacity - self.attendees.count()

# This class keeps track of trees planted related to a story.
class TreePlanting(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    planted_by = models.CharField(max_length=100, help_text="Visitor name or 'Anonymous'")
    planted_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Tree for {self.story.title} by {self.planted_by}"
