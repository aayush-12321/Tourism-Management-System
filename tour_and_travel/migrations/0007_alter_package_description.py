# Generated by Django 5.0.2 on 2024-04-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_and_travel', '0006_alter_package_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]
