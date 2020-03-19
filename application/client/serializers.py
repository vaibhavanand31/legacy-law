from rest_framework import serializers
from .models import ContactUs, Testimonial, Appointment

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone', 'query')

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ('id', 'name', 'email', 'description', 'rating')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'name', 'email', 'phone', 'dateTime', 'partner_associate')