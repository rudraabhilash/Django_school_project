# Generated by Django 5.0.6 on 2024-06-05 15:49

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