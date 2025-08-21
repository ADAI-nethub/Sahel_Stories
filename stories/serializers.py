from rest_framework import serializers
from .models import Story, Artisan, Category, Tag, Comment, Event

class EventSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_available_slots(self, obj):
        return obj.capacity - obj.attendees.count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = ["id", "bio", "community", "user"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "name", "body", "created_at"]

class StorySerializer(serializers.ModelSerializer):
    artisan = ArtisanSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    is_published = serializers.BooleanField(read_only=True)
    
    # Write-only fields for relationships
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True,
        required=False
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
            'id', 'title', 'transcript', 'audio_file', 'location',
            'artisan', 'category', 'category_id', 'tags', 'tag_ids',
            'created_at', 'published_at', 'is_published', 'comments_count'
        ]

    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()