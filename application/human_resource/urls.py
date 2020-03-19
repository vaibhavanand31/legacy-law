from django.urls import path, include
from .views import EmploymentApplicationView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('employment-application', EmploymentApplicationView)

urlpatterns = [
    path('', include(router.urls))
]