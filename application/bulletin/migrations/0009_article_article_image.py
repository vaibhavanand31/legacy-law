# Generated by Django 2.2.6 on 2020-05-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0008_auto_20200515_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank='True', upload_to='articels'),
        ),
    ]
