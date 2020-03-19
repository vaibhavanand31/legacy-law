from rest_framework import routers
from django.urls import path, include

from .views import PartnersView, PracticingAreaView

router = routers.DefaultRouter()
router.register('partners', PartnersView)
router.register('practicing-area', PracticingAreaView)

urlpatterns = [
    path('', include(router.urls))
]

