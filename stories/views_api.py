from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Story
from .serializers import StorySerializer
from rest_framework.pagination import PageNumberPagination

class StoryPagination(PageNumberPagination):
    page_size = 10





class StoryFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    artisan = filters.NumberFilter(field_name='artisan__user__id')
    tag = filters.CharFilter(field_name='tags__name', lookup_expr='iexact')
    q = filters.CharFilter(method='filter_search')

    class Meta:
        model = Story
        fields = ['category', 'artisan', 'tag']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(transcript__icontains=value) |
            Q(artisan__user__first_name__icontains=value) |
            Q(artisan__user__last_name__icontains=value) |
            Q(location__icontains=value)
        ).distinct()


class StoryListAPI(generics.ListAPIView):
    """
    API Endpoint: GET /api/stories/
    Returns published stories with filtering, search, and pagination.
    """
    queryset = Story.objects.filter(published_at__isnull=False).order_by('-published_at')
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StoryFilter
    pagination_class = StoryPagination  # ✅ now pagination is applied



class StoryDetailAPI(generics.RetrieveAPIView):
    """
    API Endpoint: GET /api/stories/1/
    Returns a single published story by ID.
    """
    queryset = Story.objects.filter(published_at__isnull=False)
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'