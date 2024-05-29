from django.db import models

# Create your models here.




class attendance(models.Model):
      student_id =  models.IntegerField(null=True)
      entry_time = models.DateTimeField()
      exit_time =  models.DateTimeField()
      date= models.DateField(null=True)

def __str__(self):
    return f"{self.entry_time} {self.exit_time} {self.date}"


class standard(models.Model):
     total_students = models.IntegerField(null=True)
     class_teacher = models.CharField(max_length=255)
     monitor_student_id =  models.IntegerField(null=True)

def __str__(self):
    return f"{self.total_students} {self.class_teacher}  { self.monitor_student_id}"



class schedule(models.Model):
     class_id= models.IntegerField(null=True)
     schedule_order= models.CharField(max_length=255)

def __str__(self):
    return f"{self.class_id} {self.schedule_order}"
