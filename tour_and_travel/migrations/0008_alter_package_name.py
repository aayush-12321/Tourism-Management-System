# Generated by Django 5.0.2 on 2024-04-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_and_travel', '0007_alter_package_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
