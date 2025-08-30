# Fichier : stories/admin.py
# Ce fichier controle comment nos modeles apparaissent dans le panneau d'administration Django

from django.contrib import admin  # On importe les outils d'administration
from .models import Artisan, Story, TreePlanting, Category, Tag  # On importe nos modeles

# -------------------------------------------------------------------
# Administration des Artisans
# -------------------------------------------------------------------
@admin.register(Artisan)
class ArtisanAdmin(admin.ModelAdmin):
    # Colonnes a afficher dans la liste des artisans
    list_display = ('user', 'community', 'bio')
    # Champs utilisables pour la recherche
    search_fields = ('user__username', 'community')
    # Champs qui ne peuvent pas etre modifies
    readonly_fields = ('user',)

# -------------------------------------------------------------------
# Administration des Histoires
# -------------------------------------------------------------------
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    # Colonnes a afficher dans la liste des histoires
    list_display = ('title', 'artisan', 'published_at', 'views')
    # Champs qu'on peut modifier directement dans la liste
    list_editable = ('published_at',)
    # Champs utilisables pour la recherche
    search_fields = ('title', 'artisan__user__username')
    # Filtres qui apparaissent sur le cote
    list_filter = ('published_at', 'artisan')

# -------------------------------------------------------------------
# Administration des Plantations d'Arbres
# -------------------------------------------------------------------
@admin.register(TreePlanting)
class TreePlantingAdmin(admin.ModelAdmin):
    # Colonnes a afficher dans la liste des plantations
    list_display = ('story', 'planted_by', 'status', 'planted_at')
    # Filtres disponibles
    list_filter = ('status', 'planted_at')
    # Champs utilisables pour la recherche
    search_fields = ('story__title', 'planted_by')
    # Champs qui se remplissent automatiquement
    readonly_fields = ('planted_at', 'actually_planted_at')

# -------------------------------------------------------------------
# Administration des Categories et Tags
# -------------------------------------------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Colonnes a afficher
    list_display = ('name', 'slug')
    # Le slug se remplit automatiquement a partir du nom
    prepopulated_fields = {"slug": ("name",)}
    # Champs utilisables pour la recherche
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Colonnes a afficher
    list_display = ('name', 'slug')
    # Le slug se remplit automatiquement a partir du nom
    prepopulated_fields = {"slug": ("name",)}
    # Champs utilisables pour la recherche
    search_fields = ('name',)