from django.contrib import admin
from .models import Artisan, Story, TreePlanting
from .models import Category, Tag, Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'artisan', 'published_at')
    list_editable = ('published_at',)


admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Artisan)
admin.site.register(Story)
admin.site.register(TreePlanting)
