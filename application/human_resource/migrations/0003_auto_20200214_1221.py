# Generated by Django 2.2.6 on 2020-02-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0002_auto_20200214_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment_application',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employment_application',
            name='experience_years',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employment_application',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='employment_application',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='employment_application',
            name='phone',
            field=models.FloatField(default=None, max_length=12),
        ),
    ]