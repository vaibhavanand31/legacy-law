# Generated by Django 2.2.6 on 2020-02-19 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='dateTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='dateTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
