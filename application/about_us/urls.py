from django.urls import path, include
from .views import ServiceAddressView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('service-address', ServiceAddressView)

urlpatterns = [
    path('', include(router.urls))
]