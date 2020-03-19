from rest_framework import routers
from .views import NewsView, EventView, ArticleView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('news', NewsView)
router.register('event', EventView)
router.register('article', ArticleView)

urlpatterns = [
    path('', include(router.urls))
]