from django.contrib import admin
from .models import Artisan, Story, TreePlanting, Category, Tag

# Define StoryAdmin first
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'artisan', 'published_at')
    list_editable = ('published_at',)

# Unregister if already registered (avoids AlreadyRegistered error)
try:
    admin.site.unregister(Story)
except admin.sites.NotRegistered:
    pass

# Register models
admin.site.register(Story, StoryAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Artisan)
admin.site.register(TreePlanting)
