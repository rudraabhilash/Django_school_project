from django.db import models
from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField(null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    doj = models.DateField()
    address = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    standard_id = models.IntegerField(null=True)
    creator_id = models.IntegerField(null=True)
    last_user_id = models.IntegerField(null=True)
    is_active = models.IntegerField(null=True)
    session = models.CharField(max_length=255)
    photo_location = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.roll_no} {self.firstname} {self.lastname} {self.dob} {self.doj} {self.address} {self.height} {self.gender} {self.standard_id} {self.last_user_id} {self.is_activate} {self.session} {self.photo_location}"

class Parent(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    creator_id = models.IntegerField(null=True)
    last_user_id = models.IntegerField(null=True)

    