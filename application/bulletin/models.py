from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class News(models.Model):
    date = models.DateField(auto_now_add=True)
    heading = models.CharField(max_length=200, blank=False, unique=True)
    sub_heading = models.CharField(max_length=500, blank=True, default=heading)
    content = models.TextField(max_length=10000, blank=False)
    source = models.CharField(max_length=200, blank=True, default=None)
    publisher = models.CharField(
        max_length=200, blank=False, default='Legacy Law')
    news_image = models.ImageField(upload_to='news', blank='True')

    def preview(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.news_image))

    def __str__(self):
        return self.heading


class Event(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=False, default=title)
    street_address = models.CharField(max_length=200, blank=True, default=None)
    city = models.CharField(max_length=30, blank=True, default=None)
    state = models.CharField(max_length=20, blank=True, default=None)
    event_image = models.ImageField(upload_to='events', blank='True')

    def preview(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.event_image))

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    writer = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=20000, blank=False)
    date = models.DateField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articels', blank='True')

    def preview(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.article_image))


    def __str__(self):
        return self.title
