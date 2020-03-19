from django.contrib import admin
from .models import News, Event, Article
from django.utils.html import format_html

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'heading')
    readonly_fields = ['preview']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'city')
    readonly_fields = ['preview']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')