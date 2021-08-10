from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from financialNewsApp.models import News
from financialNewsApp.serializers import NewsSerializer
from rest_framework import mixins, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class NewsList(mixins.ListModelMixin,
               viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'symbol__short_name', 'title', 'description', 'pub_date']
    search_fields = ['title', 'description', 'pub_date']

    # cache for 10 minutes
    @method_decorator(cache_page(60 * 10))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
