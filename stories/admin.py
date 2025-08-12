from django.contrib import admin
from .models import Artisan, Story, TreePlanting
from .models import Category, Tag

admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Artisan)
admin.site.register(Story)
admin.site.register(TreePlanting)
