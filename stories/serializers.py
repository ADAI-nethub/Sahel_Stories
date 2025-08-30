# Fichier : serializers.py
# Ce sont des "traducteurs" pour nos modeles de base de donnees.
# Ils transforment les objets Python en JSON pour le frontend,
# et transforment le JSON en objets Python pour la sauvegarde.

from rest_framework import serializers   # Aide avec JSON <-> Python
from django.utils import timezone        # Gere le temps et la date
from django.contrib.auth.models import User  # Modele d'utilisateur integre de Django
from .models import Story, Artisan, Category, Tag, Comment, Event  # Nos modeles de donnees


# Transforme un utilisateur Django en JSON (seulement les informations de base)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['date_joined']  # L'utilisateur ne peut pas changer cela


# Les categories aident a organiser les histoires
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]  # Le slug est genere automatiquement


# Les tags sont comme des hashtags pour les histoires
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]


# Le conteur (nous l'appelons Artisan)
class ArtisanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Montre seulement le nom
    story_count = serializers.SerializerMethodField()      # Compte ses histoires publiees

    class Meta:
        model = Artisan
        fields = ["id", "user", "bio", "community", "story_count", "created_at"]
        read_only_fields = ["created_at"]

    # Compte seulement les histoires qui sont publiees
    def get_story_count(self, obj):
        return obj.stories.filter(published_at__isnull=False).count()


# Commentaires laisses par les personnes sur une histoire
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    story_title = serializers.CharField(source='story.title', read_only=True)  # Montre le nom de l'histoire

    class Meta:
        model = Comment
        fields = ["id", "story", "story_title", "user", "name", "email", "body",
                  "created_at", "active"]
        read_only_fields = ["created_at", "active"]
        extra_kwargs = {
            'email': {'write_only': True}  # Ne montre jamais l'email dans la reponse
        }


# Evenements comme des festivals ou des ateliers
class EventSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField()  # Combien de places restantes
    is_full = serializers.SerializerMethodField()          # L'evenement est-il complet ?
    can_register = serializers.SerializerMethodField()     # Cet utilisateur peut-il s'inscrire ?

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date_time', 'location', 'capacity',
            'available_slots', 'is_full', 'can_register'
        ]
        read_only_fields = ['available_slots', 'is_full', 'can_register']

    # Combien de places vides restantes
    def get_available_slots(self, obj):
        return obj.capacity - obj.attendees.count()

    # L'evenement est-il deja complet ?
    def get_is_full(self, obj):
        return obj.attendees.count() >= obj.capacity

    # L'utilisateur actuel peut-il s'inscrire ?
    def get_can_register(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return not obj.attendees.filter(id=request.user.id).exists()
        return False


# Serializer pour creer ou mettre a jour une histoire
class StoryWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',   # Se connecte au champ reel dans le modele
        write_only=True,
        required=False,
        allow_null=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source='tags',
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Story
        fields = [
            'title', 'transcript', 'audio_file', 'location', 'latitude', 'longitude',
            'category_id', 'tag_ids'
        ]

    # Verifie les regles du fichier audio
    def validate_audio_file(self, value):
        if value:
            max_size = 10 * 1024 * 1024  # 10 MB maximum
            if value.size > max_size:
                raise serializers.ValidationError("Fichier audio trop volumineux. Taille max: 10MB.")
            valid_extensions = ['.mp3', '.wav', '.ogg', '.m4a']
            if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
                raise serializers.ValidationError("Format de fichier non supporte.")
        return value

    # Lors de la sauvegarde, lie l'histoire a l'artisan connecte
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['artisan'] = request.user.artisan
        return super().create(validated_data)


# Serializer pour lire les details d'une histoire (pour le frontend)
class StoryReadSerializer(serializers.ModelSerializer):
    artisan = ArtisanSerializer(read_only=True)     # Montre les infos du conteur
    category = CategorySerializer(read_only=True)   # Montre les infos de la categorie
    tags = TagSerializer(many=True, read_only=True) # Montre les tags
    comments_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    is_published = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = [
            'id', 'title', 'transcript', 'audio_file', 'location', 'latitude', 'longitude',
            'artisan', 'category', 'tags', 'comments_count', 'average_rating', 'duration',
            'created_at', 'published_at', 'is_published', 'views'
        ]
        read_only_fields = ['created_at', 'published_at', 'views']

    # Compte les commentaires actifs
    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()

    # Note moyenne de l'histoire
    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return None

    # Retourne la duree si l'histoire a un audio
    def get_duration(self, obj):
        if hasattr(obj, 'duration'):
            return obj.duration
        return None

    # Verifie si l'histoire est publiee
    def get_is_published(self, obj):
        return obj.is_published


# Serializer intelligent qui choisit la bonne version
class StorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # Utilise le serializer "read" lors de l'envoi de donnees
        return StoryReadSerializer(instance, context=self.context).to_representation(instance)

    def to_internal_value(self, data):
        # Utilise le serializer "write" lors de la reception de donnees
        return StoryWriteSerializer(context=self.context).to_internal_value(data)

    class Meta:
        model = Story
        fields = '__all__'  # Prend tout depuis le modele