from django.db import models

# Create your models here.

class ServiceAddress(models.Model):
    address_choices = (
        ('Head Office', 'Head Office'),
        ('Chamber Addres', 'Chamber Addres'),
        ('Other Offices', 'Other Offices'),
    )
    street_address = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=20, null=False)
    pincode = models.IntegerField(null=False)
    address_type = models.CharField(choices = address_choices, null=True, max_length=20, default='address_choices[2]')