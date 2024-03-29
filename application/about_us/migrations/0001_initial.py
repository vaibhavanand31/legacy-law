# Generated by Django 2.2.6 on 2020-02-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('address_type', models.CharField(default=('Other Offices', 'oa'), max_length=20, null=True, verbose_name=(('Head Office', 'ho'), ('Chamber Addres', 'ca'), ('Other Offices', 'oa')))),
            ],
        ),
    ]
