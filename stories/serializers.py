from rest_framework import serializers
from .models import Story, Artisan, Category, Tag, Comment


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
    is_published = serializers.BooleanField(source='published_at', read_only=True)

    class Meta:
        model = Story
        fields = [
            'id', 'title', 'transcript', 'audio_file', 'location',
            'artisan', 'category', 'tags', 'created_at', 'published_at',
            'is_published', 'comments_count'
        ]

    def get_comments_count(self, obj):
        return obj.comments.filter(active=True).count()

    def get_is_published(self, obj):
        return obj.published_at is not None
