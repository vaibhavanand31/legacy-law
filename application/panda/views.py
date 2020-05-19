from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from application.pagination import StandardResultsSetPagination
from .models import PracticingArea, Partners
from .serializer import PartnerSerializer, PartnersSerializer, PracticingAreaSerializer

# Create your views here.


class PracticingAreaView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = PracticingArea.objects.all()
    serializer_class = PracticingAreaSerializer
    pagination_class = StandardResultsSetPagination


class PartnerView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Partners.objects.all().order_by('first_name')
    serializer_class = PartnerSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug_field'


class PartnersView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Partners.objects.all().order_by('first_name')
    serializer_class = PartnersSerializer
    pagination_class = StandardResultsSetPagination
