# 📘 stories/apps.py
# This file tells Django about our "stories" app 🎨

from django.apps import AppConfig

# 🏷️ Each app needs a "Config class" so Django knows how to set it up
class StoriesConfig(AppConfig):
    # 🔢 Use a big number ID for new database tables
    default_auto_field = 'django.db.models.BigAutoField'
    # 🏠 Name of the app (matches the folder)
    name = 'stories'
