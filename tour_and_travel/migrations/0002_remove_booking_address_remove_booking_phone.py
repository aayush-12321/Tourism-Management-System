# Generated by Django 5.0.2 on 2024-04-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_and_travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
    ]
