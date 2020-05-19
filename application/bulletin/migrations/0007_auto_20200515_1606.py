# Generated by Django 2.2.6 on 2020-05-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0006_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='sub_heading',
            field=models.CharField(blank=True, default=models.CharField(max_length=200, unique=True), max_length=500),
        ),
    ]