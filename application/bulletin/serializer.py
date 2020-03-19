from rest_framework import serializers
from .models import Article, Event, News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'date', 'heading', 'sub_heading', 'content', 'source', 'publisher', 'news_image')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'start_date', 'end_date', 'description', 'street_address', 'city', 'state', 'event_image')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'writer', 'content')