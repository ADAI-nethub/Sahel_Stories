# 📘 stories/admin.py
# This file controls how our models appear in the Django Admin panel 🛠️

from django.contrib import admin
from .models import Artisan, Story, TreePlanting, Category, Tag


# -------------------------------------------------------------------
# 👩‍🎨 Artisan Admin
# -------------------------------------------------------------------
@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'bio')  # Columns to show
    search_fields = ('user__username', 'community')  # Search bar for admin
    readonly_fields = ('user',)  # Can't edit the linked user here

# -------------------------------------------------------------------
# 📖 Story Admin
# -------------------------------------------------------------------
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'artisan', 'published_at', 'views')  # Show key info
    list_editable = ('published_at',)  # Quick edit published date
    search_fields = ('title', 'artisan__user__username')  # Add search
    list_filter = ('published_at', 'artisan')  # Add filters on side

# -------------------------------------------------------------------
# 🌳 TreePlanting Admin
# -------------------------------------------------------------------
@admin.register(TreePlanting)
class TreePlantingAdmin(admin.ModelAdmin):
    list_display = ('story', 'planted_by', 'status', 'planted_at')  # Show key info
    list_filter = ('status', 'planted_at')  # Filter by status & date
    search_fields = ('story__title', 'planted_by')  # Quick search
    readonly_fields = ('planted_at', 'actually_planted_at')  # Auto fields

# -------------------------------------------------------------------
# 🏷️ Category & Tag Admin
# -------------------------------------------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}  # Auto-fill slug from name
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
