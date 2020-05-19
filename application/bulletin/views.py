from django.shortcuts import render
from application.pagination import StandardResultsSetPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from .models import News, Event, Article
from .serializer import NewsSerializer, EventSerializer, ArticleSerializer

# Create your views here.


class NewsView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'heading'


class EventView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Event.objects.all().order_by('-start_date')
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'title'


class ArticleView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'title'
