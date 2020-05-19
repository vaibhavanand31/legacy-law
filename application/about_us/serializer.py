from rest_framework import serializers
from .models import ServiceAddress


class ServiceAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAddress
        fields = ('id', 'street_address', 'city',
                  'state', 'pincode', 'address_type')
