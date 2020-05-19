from rest_framework import routers
from django.urls import path, include

from .views import PartnerView, PartnersView, PracticingAreaView

router = routers.DefaultRouter()
router.register('partners', PartnersView)
router.register('partner', PartnerView)
router.register('practicing-area', PracticingAreaView)

urlpatterns = [
    path('', include(router.urls))
]
