from django.db import models

class Marksheet(models.Model):
    SESSION_CHOICES = [
        ('mid_year', 'Mid Year'),#figure this out
        ('end_year', 'End Year'),
    ]

    
    student_id = models.IntegerField(null=True)
    english_marks = models.IntegerField(null=True)
    hindi_marks = models.IntegerField(null=True)
    maths_marks = models.IntegerField(null=True)
    science_marks = models.IntegerField(null=True)
    socialstudy_marks = models.IntegerField(null=True)
    session = models.CharField(max_length=20, choices=SESSION_CHOICES)

    def __str__(self):
        return f"Student ID: {self.student_id}, Session: {self.get_session_display()}"
    


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teachers = models.CharField(max_length=100)
    books = models.CharField(max_length=100)

    