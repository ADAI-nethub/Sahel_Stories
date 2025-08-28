from rest_framework import serializers  # Tools to help turn data into JSON and back
from django.utils import timezone  # To work with dates and times
from django.contrib.auth.models import User  # Built-in user info from Django
from .models import Story, Artisan, Category, Tag, Comment, Event  # Our own data models

# Turn a Django user into a JSON-friendly object
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['date_joined']

# Used to organize stories into different categories
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]

# Tiny labels used to describe stories (like hashtags)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["slug"]

# The storyteller (called an "Artisan")
class ArtisanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Just show the name, not all user info
    story_count = serializers.SerializerMethodField()  # Count stories by this artisan

    class Meta:
        model = Artisan
        fields = ["id", "user", "bio", "community", "story_count", "created_at"]
        read_only_fields = ["created_at"]

    # 👇 This method counts only stories that are published
    def get_story_count(self, obj):
        return obj.stories.filter(published_at__isnull=False).count()

# Comments left by people on a story
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    story_title = serializers.CharField(source='story.title', read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "story", "story_title", "user", "name", "email", "body",
                  "created_at", "active"]
        read_only_fields = ["created_at", "active"]
        extra_kwargs = {
            'email': {'write_only': True}  # Don't show email in responses
        }

# Events like storytelling festivals or workshops
class EventSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField()
    is_full = serializers.SerializerMethodField()
    can_register = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date_time', 'location', 'capacity',
            'available_slots', 'is_full', 'can_register'
        ]
        read_only_fields = ['available_slots', 'is_full', 'can_register']

    def get_available_slots(self, obj):
        return obj.capacity - obj.attendees.count()

    def get_is_full(self, obj):
        return obj.attendees.count() >= obj.capacity

    def get_can_register(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return not obj.attendees.filter(id=request.user.id).exists()
        return False

# Serializer for creating or updating a story
class StoryWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  # Links to actual field in model
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
            # ❌ is_published is NOT included because it's not in the database
        ]

    def validate_audio_file(self, value):
        if value:
            max_size = 10 * 1024 * 1024  # 10 MB max
            if value.size > max_size:
                raise serializers.ValidationError("Audio file too large. Max size is 10MB.")
            valid_extensions = ['.mp3', '.wav', '.ogg', '.m4a']
            if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
                raise serializers.ValidationError("Unsupported file format.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['artisan'] = request.user.artisan
        return super().create(validated_data)

# Serializer for reading story details (sending story to frontend)
class StoryReadSerializer(serializers.ModelSerializer):
    artisan = ArtisanSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    is_published = serializers.SerializerMethodField()  # ✅ This shows whether story is published

    class Meta:
        model = Story
        fields = [
            'id', 'title', 'transcript', 'audio_file', 'location', 'latitude', 'longitude',
            'artisan', 'category', 'tags', 'comments_count', 'average_rating', 'duration',
            'created_at', 'published_at', 'is_published', 'views'
        ]
        read_only_fields = ['created_at', 'published_at', 'views']

    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return None

    def get_duration(self, obj):
        if hasattr(obj, 'duration'):
            return obj.duration
        return None

    def get_is_published(self, obj):
        return obj.is_published  # ✅ Uses the @property on your model

# Smart serializer that switches between read & write versions
class StorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return StoryReadSerializer(instance, context=self.context).to_representation(instance)

    def to_internal_value(self, data):
        return StoryWriteSerializer(context=self.context).to_internal_value(data)

    class Meta:
        model = Story
        fields = '__all__'  # Automatically includes everything from the model
