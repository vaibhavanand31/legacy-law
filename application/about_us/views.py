from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from application.pagination import StandardResultsSetPagination

# models & serializer
from .models import ServiceAddress
from .serializer import ServiceAddressSerializer


# Create your views here.
class ServiceAddressView(GenericViewSet, ListModelMixin):
    queryset = ServiceAddress.objects.all().order_by('address_choices')
    serializer_class = ServiceAddressSerializer
    pagination_class = StandardResultsSetPagination
