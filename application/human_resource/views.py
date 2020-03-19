from django.shortcuts import render

from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
# models & serializer
from .models import Employment_application
from .serializer import EmploymentApplicationSerializer

# Create your views here.

class EmploymentApplicationView(GenericViewSet, CreateModelMixin):
    queryset = Employment_application.objects.all()
    serializer_class = EmploymentApplicationSerializer