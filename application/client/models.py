from django.db import models
from datetime import datetime    
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True, default=None)
    email = models.EmailField(max_length=150, blank=True, default=None)
    description = models.TextField(max_length=750, blank=False)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, default=None)
    dateTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=False, default=None)
    email = models.EmailField(max_length=150, blank=False, default=None)
    phone = models.FloatField(max_length=12, blank=False, default=None)
    query = models.TextField(max_length=1000, blank=False, default=None)
    dateTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    appointment_status_choice = (
        ('appointed', 'appointed'),
        ('unassigned', 'unassigned',),
        ('completed', 'completed')
    )

    name = models.CharField(max_length=100, blank=False, default=None)
    email = models.EmailField(max_length=150, blank=False, default=None)
    phone = models.FloatField(max_length=12, blank=False, default=None)
    dateTime = models.DateTimeField()
    partner_associate = models.ForeignKey('panda.Partners', on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=appointment_status_choice,max_length=50, default=appointment_status_choice[1])

    def __str__(self):
        return self.name