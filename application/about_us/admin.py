from django.contrib import admin
from .models import ServiceAddress
# Register your models here.

@admin.register(ServiceAddress)
class ServiceAddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'address_type')