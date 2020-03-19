from django.contrib import admin
from .models import Testimonial, ContactUs, Appointment
from panda.models import Partners

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    def get_partner_associated(self, obj):
        return obj.partner_associate.first_name + ' ' + obj.partner_associate.last_name

    list_display = ('name', 'get_partner_associated','status', 'dateTime')
