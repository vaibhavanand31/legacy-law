from django.urls import path, include
from .views import ContactUsView, TestimonialView, AppointmentView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact-us', ContactUsView)
router.register('testimonial', TestimonialView)
router.register('appointment', AppointmentView)

urlpatterns = [
    path('', include(router.urls))
]
