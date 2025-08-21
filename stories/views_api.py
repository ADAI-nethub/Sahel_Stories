# stories/views_api.py
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django_filters import rest_framework as filters
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Story, Event
from .serializers import StorySerializer, EventSerializer


# -----------------------------
# Event API
# -----------------------------
class EventListAPI(generics.ListAPIView):
    """GET /api/events/"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


# -----------------------------
# User API
# -----------------------------
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    artisan = getattr(request.user, "artisan", None)
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "name": request.user.get_full_name() or request.user.username,
        "bio": getattr(artisan, "bio", ""),
        "community": getattr(artisan, "community", ""),
        "is_authenticated": True,
    })


# -----------------------------
# Pagination
# -----------------------------
class StoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# -----------------------------
# Filters
# -----------------------------
class StoryFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name", lookup_expr="iexact")
    artisan = filters.NumberFilter(field_name="artisan__user__id")
    tag = filters.CharFilter(field_name="tags__name", lookup_expr="iexact")
    q = filters.CharFilter(method="filter_search")

    class Meta:
        model = Story
        fields = ["category", "artisan", "tag"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(transcript__icontains=value) |
            Q(artisan__user__first_name__icontains=value) |
            Q(artisan__user__last_name__icontains=value) |
            Q(location__icontains=value)
        ).distinct()


# -----------------------------
# Story API
# -----------------------------
class StoryListAPI(generics.ListAPIView):
    """GET /api/stories/"""
    queryset = Story.objects.filter(published_at__isnull=False).order_by("-published_at")
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StoryFilter
    pagination_class = StoryPagination


class StoryDetailAPI(generics.RetrieveAPIView):
    """GET /api/stories/<id>/"""
    queryset = Story.objects.filter(published_at__isnull=False)
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


class StoryCreateAPI(generics.CreateAPIView):
    """POST /api/stories/create/"""
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        artisan = self.request.user.artisan
        serializer.save(artisan=artisan)
