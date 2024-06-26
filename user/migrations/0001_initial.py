# Generated by Django 5.0.6 on 2024-05-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=100)),
                ('is_active', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField()),
                ('role', models.CharField(max_length=50)),
            ],
        ),
    ]
