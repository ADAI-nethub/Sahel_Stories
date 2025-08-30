# Fichier : stories/models.py
from django.db import models  # Pour creer des modeles de base de donnees
from django.utils import timezone  # Pour avoir l'heure actuelle
from django.utils.translation import gettext_lazy as _  # Pour les traductions

# Modele pour representer la plantation d'un arbre
class TreePlanting(models.Model):
    # Les differents statuts possibles pour un arbre
    class Status(models.TextChoices):
        PENDING = 'pending', _('En attente - Promesse faite')
        PLANTED = 'planted', _('Plante - Arbre en terre')
        VERIFIED = 'verified', _('Verifie - Arbre controle')
        FAILED = 'failed', _('Echoue - Impossible de planter')

    # L'histoire liee a cette plantation
    story = models.ForeignKey(
        'Story',  # Relation avec le modele Story
        on_delete=models.CASCADE,  # Si l'histoire est supprimee, la plantation aussi
        related_name='tree_plantings'  # Nom pour acceder aux plantations depuis une histoire
    )
    # Le nom de la personne qui a plante l'arbre
    planted_by = models.CharField(max_length=100)
    # La date et l'heure de la creation de l'enregistrement
    planted_at = models.DateTimeField(auto_now_add=True)
    # La latitude de l'endroit ou l'arbre est plante (optionnel)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # La longitude de l'endroit ou l'arbre est plante (optionnel)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # Le statut actuel de la plantation
    status = models.CharField(
        max_length=10,
        choices=Status.choices,  # Les choix possibles venant de la classe Status
        default=Status.PENDING,  # Statut par defaut
    )
    # La date et l'heure reelles ou l'arbre a ete plante (optionnel)
    actually_planted_at = models.DateTimeField(null=True, blank=True)

    # Methode pour marquer un arbre comme plante
    def mark_as_planted(self):
        self.status = self.Status.PLANTED  # Change le statut
        self.actually_planted_at = timezone.now()  # Met la date actuelle
        self.save(update_fields=['status', 'actually_planted_at'])  # Sauvegarde

    # Comment afficher cet objet en texte
    def __str__(self):
        return f"Arbre pour '{self.story.title}' par {self.planted_by} [{self.get_status_display()}]"

# Modele pour representer un artisan
class Artisan(models.Model):
    # Lien avec un utilisateur du systeme (un seul profil artisan par utilisateur)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='artisan_profile')
    # La biographie de l'artisan
    bio = models.TextField(blank=True)
    # La communaute de l'artisan
    community = models.CharField(max_length=100, blank=True)
    # La date de creation du profil
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username  # Affiche le nom d'utilisateur

# Modele pour representer une histoire
class Story(models.Model):
    # Le titre de l'histoire
    title = models.CharField(max_length=200)
    # Le contenu de l'histoire
    content = models.TextField()
    # L'artisan qui a ecrit l'histoire
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, related_name='stories')
    # La date de publication (optionnelle)
    published_at = models.DateTimeField(null=True, blank=True)
    # Le nombre de vues de l'histoire
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title  # Affiche le titre

# Modele pour representer une categorie
class Category(models.Model):
    # Le nom de la categorie
    name = models.CharField(max_length=100)
    # Le slug (version URL du nom)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name  # Affiche le nom

# Modele pour representer un tag
class Tag(models.Model):
    # Le nom du tag
    name = models.CharField(max_length=100)
    # Le slug (version URL du nom)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name  # Affiche le nom

# Modele pour representer un evenement
class Event(models.Model):
    # Le titre de l'evenement
    title = models.CharField(max_length=200)
    # La description de l'evenement
    description = models.TextField()
    # La date et l'heure de l'evenement
    date_time = models.DateTimeField()
    # Le lieu de l'evenement
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title  # Affiche le titre

# Modele pour representer un commentaire
class Comment(models.Model):
    # L'histoire sur laquelle porte le commentaire
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    # Le nom de l'auteur du commentaire
    author_name = models.CharField(max_length=100)
    # Le contenu du commentaire
    content = models.TextField()
    # La date de creation du commentaire
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.author_name} sur {self.story.title}"