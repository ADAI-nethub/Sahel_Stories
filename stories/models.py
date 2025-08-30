# stories/models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class TreePlanting(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending - Promise Made')
        PLANTED = 'planted', _('Planted - Tree in Ground')
        VERIFIED = 'verified', _('Verified - Tree Checked')
        FAILED = 'failed', _('Failed - Couldn’t Plant')

    story = models.ForeignKey(
        'Story',
        on_delete=models.CASCADE,
        related_name='tree_plantings'
    )
    planted_by = models.CharField(max_length=100)
    planted_at = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    actually_planted_at = models.DateTimeField(null=True, blank=True)

    def mark_as_planted(self):
        self.status = self.Status.PLANTED
        self.actually_planted_at = timezone.now()
        self.save(update_fields=['status', 'actually_planted_at'])

    def __str__(self):
        return f"Tree for '{self.story.title}' by {self.planted_by} [{self.get_status_display()}]"



# Create an Artisan model based on the structure of your project
class Artisan(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='artisan_profile')
    bio = models.TextField(blank=True)
    community = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

# Create an Story model based on the structure of your project
class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='stories')
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    

# Create an Category model based on the structure of your project
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
# Create an Tag model based on the structure of your project
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    # Create an event model based on the structure of your project
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

 # Create an comment model based on the structure of your project
class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.story.title}"

        

    



