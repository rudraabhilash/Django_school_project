from django.db import models
from django.utils import timezone
class User(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True) 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=100)
    is_active =models.CharField(max_length=50)
    date_of_joining = models.DateField()
    role = models.CharField(max_length=50)

   