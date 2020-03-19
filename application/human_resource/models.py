from django.db import models

# Create your models here.
class Employment_application(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False, default=None)
    last_name = models.CharField(max_length=30, null=False, blank=False, default=None)
    email = models.EmailField(max_length=50, null=False, blank=False, default=None)
    phone = models.FloatField(max_length=12, null=False, blank=False, default=None)
    experience_years = models.IntegerField(default=0, null=False, blank=False)
    designation = models.CharField(max_length=30, null=True, blank=True, default=None)
    resume = models.FileField(upload_to="resume", blank=True, null=True)