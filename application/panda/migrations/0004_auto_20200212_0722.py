# Generated by Django 2.2.6 on 2020-02-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0003_auto_20200212_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='designation',
            field=models.CharField(choices=[('Senior Partner', 'sp'), ('Partner', 'p'), ('Associates', 'a')], max_length=50),
        ),
    ]