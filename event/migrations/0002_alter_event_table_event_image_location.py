# Generated by Django 5.0.6 on 2024-06-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_table',
            name='event_image_location',
            field=models.ImageField(upload_to='event/static'),
        ),
    ]
