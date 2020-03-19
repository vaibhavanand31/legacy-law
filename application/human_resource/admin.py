from django.contrib import admin
from .models import Employment_application
from admin_ordering.admin import OrderableAdmin

# Register your models here.

@admin.register(Employment_application)
class ApplicationsAdmin(admin.ModelAdmin):
    ordering_field = '-id'
    list_display = ('first_name', 'last_name')
