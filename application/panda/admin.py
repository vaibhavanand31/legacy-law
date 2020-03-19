from django.contrib import admin
from .models import Partners, PracticingArea
from django.utils.html import format_html

# Register your models here.

@admin.register(Partners)
class PartnerAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return format_html(
            '<img src="{url}" width="150" height="150" />'.format(url = obj.display_picture.url)
        )
    list_display = ('first_name', 'last_name', 'email', 'phone', 'slug_field')
    readonly_fields = ['preview',]

@admin.register(PracticingArea)
class PracticingAreaAdmin(admin.ModelAdmin):
    list_display = ('title', )