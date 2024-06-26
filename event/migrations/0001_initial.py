# Generated by Django 5.0.6 on 2024-05-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('event_duration', models.IntegerField()),
                ('event_guest', models.CharField(max_length=255)),
                ('event_participation_count', models.IntegerField(null=True)),
                ('event_cost', models.IntegerField(null=True)),
                ('event_type', models.CharField(max_length=255)),
                ('event_winner_id', models.IntegerField(null=True)),
                ('event_image_location', models.CharField(max_length=255)),
            ],
        ),
    ]
