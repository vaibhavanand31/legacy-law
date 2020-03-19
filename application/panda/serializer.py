from rest_framework import serializers
from .models import PracticingArea, Partners

class PracticingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticingArea
        fields = ('id', 'discription', 'specialization_1', 'specialization_2', 'specialization_3', 'specialization_4', 'specialization_5', 'specialization_6', 'specialization_7', 'specialization_8', 'specialization_9', 'specialization_10')

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'first_name', 'last_name', 'slug_field', 'designation', 'city', 'short_description', 'long_description', 'llb_university', 'llb_city', 'mbl_university', 'mbl_city', 'bar_admition', 'bar_membership_city', 'email', 'address', 'phone', 'display_picture')
        lookup_field = 'slug_field'
        extra_kwargs = {
            'url': {'lookup_field': 'slug_field'}
        }