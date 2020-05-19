from django.db import models

# Create your models here


class PracticingArea(models.Model):
    title = models.CharField(blank=False, max_length=50, default=None)
    discription = models.TextField(blank=False, max_length=10000, default=None)
    specialization_1 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_2 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_3 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_4 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_5 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_6 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_7 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_8 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_9 = models.CharField(
        max_length=100, default=None, blank=True)
    specialization_10 = models.CharField(
        max_length=100, default=None, blank=True)

    def __str__(self):
        return self.title


class Partners(models.Model):
    # Options
    Designations = (
        ('Managing Partner', 'Managing Partner'),
        ('Senior Partner', 'Senior Partner'),
        ('Partner', 'Partner'),
        ('Principal Associate', 'Principal Associate'),
        ('Senior Associate', 'Senior Associate'),
        ('Associate', 'Associate'),
        ('Intern', 'Intern'),
    )
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    slug_field = models.SlugField(
        max_length=60, unique=True, help_text="Generally Use 'FirstName_LastName'")
    designation = models.CharField(
        choices=Designations, max_length=50, blank=False)
    city = models.CharField(max_length=20, blank=False)
    short_description = models.TextField(max_length=228)
    long_description = models.TextField(max_length=1028)
    llb_university = models.CharField(max_length=100)
    llb_city = models.CharField(max_length=20)
    mbl_university = models.CharField(max_length=100)
    mbl_city = models.CharField(max_length=20)
    bar_admition = models.DateField()
    bar_membership_city = models.CharField(max_length=20)
    email = models.CharField(max_length=40, blank=False)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    display_picture = models.ImageField(
        upload_to='display_picture', blank='True')

    def __str__(self):
        return self.first_name + " " + self.last_name
