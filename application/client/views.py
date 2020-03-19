from django.shortcuts import render

#GenericViewSet,   #generic view functionality
#CreateModelMixin,  # handles POSTs
#RetrieveModelMixin,  # handles GETs for 1 Company
#UpdateModelMixin,  # handles PUTs and PATCHes
#ListModelMixin):  # handles GETs for many Companies

#from rest_framework.mixins import (
#    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#)
#from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .models import ContactUs, Testimonial, Appointment
from .serializers import ContactUsSerializer, TestimonialSerializer, AppointmentSerializer

# Create your views here.

class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('datetime')
    serializer_class = ContactUsSerializer

class TestimonialView(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('datetime')
    serializer_class = TestimonialSerializer

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('datetime')
    serializer_class = AppointmentSerializer

    #def delete(request, id):
    #    Appointment.objects.get(id=id).delete()
    #    return Response()