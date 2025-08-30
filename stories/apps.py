# Fichier : stories/apps.py
# Ce fichier presente notre application "stories" a Django

from django.apps import AppConfig  # On importe la classe de base pour les applications

# Chaque application a besoin d'une "classe Config" pour que Django sache comment la configurer
class StoriesConfig(AppConfig):
    # On utilise un type d'identifiant special pour les nouvelles tables de la base de donnees
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Le nom de l'application (doit correspondre au nom du dossier)
    name = 'stories'