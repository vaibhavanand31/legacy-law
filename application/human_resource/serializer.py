from rest_framework import serializers
from .models import Employment_application

class EmploymentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment_application
        fields = ('first_name', 'last_name', 'email', 'phone', 'experience_years', 'designation', 'resume')