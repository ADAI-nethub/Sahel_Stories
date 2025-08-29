# 📘 serializers.py
# These are "translators" 🗣️ for our database models. 
# They turn Python objects into JSON for the frontend, 
# and turn JSON back into Python objects for saving.

from rest_framework import serializers   # Helps with JSON <-> Python
from django.utils import timezone        # Handles time and date
from django.contrib.auth.models import User  # Django's built-in user model
from .models import Story, Artisan, Category, Tag, Comment, Event  # Our own data models


# 👤 Turn a Django user into JSON (only basic info)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['date_joined']  # 🚫 user can't change this


# 📂 Categories help organize stories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]  # slug is made automatically


# 🏷️ Tags are like hashtags for stories
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]


# 🎤 The storyteller (we call them an Artisan)
class ArtisanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # just shows the name
    story_count = serializers.SerializerMethodField()      # counts their published stories

    class Meta:
        model = Artisan
        fields = ["id", "user", "bio", "community", "story_count", "created_at"]
        read_only_fields = ["created_at"]

    # 👉 Count only the stories that are published
    def get_story_count(self, obj):
        return obj.stories.filter(published_at__isnull=False).count()


# 💬 Comments left by people on a story
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    story_title = serializers.CharField(source='story.title', read_only=True)  # show story name too

    class Meta:
        model = Comment
        fields = ["id", "story", "story_title", "user", "name", "email", "body",
                  "created_at", "active"]
        read_only_fields = ["created_at", "active"]
        extra_kwargs = {
            'email': {'write_only': True}  # 🚫 never show email in response
        }


# 🎉 Events like festivals or workshops
class EventSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField()  # how many seats left
    is_full = serializers.SerializerMethodField()          # is the event full?
    can_register = serializers.SerializerMethodField()     # can THIS user register?

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date_time', 'location', 'capacity',
            'available_slots', 'is_full', 'can_register'
        ]
        read_only_fields = ['available_slots', 'is_full', 'can_register']

    # 👉 How many empty spots left
    def get_available_slots(self, obj):
        return obj.capacity - obj.attendees.count()

    # 👉 Is event full already?
    def get_is_full(self, obj):
        return obj.attendees.count() >= obj.capacity

    # 👉 Can the current user register?
    def get_can_register(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return not obj.attendees.filter(id=request.user.id).exists()
        return False


# ✍️ Serializer for creating or updating a story
class StoryWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',   # hook to actual field in model
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
            # ❌ no is_published here because it's a @property, not a field
        ]

    # 👉 Check audio file rules
    def validate_audio_file(self, value):
        if value:
            max_size = 10 * 1024 * 1024  # 10 MB max
            if value.size > max_size:
                raise serializers.ValidationError("Audio file too large. Max size is 10MB.")
            valid_extensions = ['.mp3', '.wav', '.ogg', '.m4a']
            if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
                raise serializers.ValidationError("Unsupported file format.")
        return value

    # 👉 When saving, tie story to logged-in artisan
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['artisan'] = request.user.artisan
        return super().create(validated_data)


# 👓 Serializer for reading story details (for frontend)
class StoryReadSerializer(serializers.ModelSerializer):
    artisan = ArtisanSerializer(read_only=True)     # show storyteller info
    category = CategorySerializer(read_only=True)   # show category info
    tags = TagSerializer(many=True, read_only=True) # show tags
    comments_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    is_published = serializers.SerializerMethodField()  # ✅ comes from @property

    class Meta:
        model = Story
        fields = [
            'id', 'title', 'transcript', 'audio_file', 'location', 'latitude', 'longitude',
            'artisan', 'category', 'tags', 'comments_count', 'average_rating', 'duration',
            'created_at', 'published_at', 'is_published', 'views'
        ]
        read_only_fields = ['created_at', 'published_at', 'views']

    # 👉 Count comments that are active
    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()

    # 👉 Average rating of story
    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return None

    # 👉 Return duration if story has audio
    def get_duration(self, obj):
        if hasattr(obj, 'duration'):
            return obj.duration
        return None

    # 👉 Check if story is published
    def get_is_published(self, obj):
        return obj.is_published


# 🧠 Smart serializer that picks the right version
class StorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        # 👉 Use "read" serializer when sending data
        return StoryReadSerializer(instance, context=self.context).to_representation(instance)

    def to_internal_value(self, data):
        # 👉 Use "write" serializer when receiving data
        return StoryWriteSerializer(context=self.context).to_internal_value(data)

    class Meta:
        model = Story
        fields = '__all__'  # grab everything from model
