from rest_framework import serializers
from .models import ServiceAddress

class ServiceAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAddress
        fields = ('street_address', 'city', 'state', 'pincode', 'address_type')