from django.db import models

# Create your models here.

class Payment(models.Model):
  student_id = models.IntegerField()
  fee_paid = models.CharField(max_length=14)
  date_of_payment = models.DateField()
  due = models.IntegerField()
  payment_mode = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.student_id}"
     

class Fee_details(models.Model):
  standard_id = models.IntegerField()
  fee = models.IntegerField()

  def __str__(self):
    return f"{self.standard_id}"
