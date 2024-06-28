from django.db import models

# Create your models here.

class Event_Table(models.Model):
  #event_id = models.IntegerField(null =True)
  event_name = models.CharField(max_length=255) 
  event_date = models.DateField()
  event_duration = models.IntegerField()
  event_guest = models.CharField(max_length=255)
  event_participation_count = models.IntegerField(null=True) 
  event_cost = models.IntegerField(null=True)
  event_type = models.CharField(max_length=255)
  event_winner_id = models.IntegerField(null=True)
  #event_image_location = models.ImageField(upload_to='event/static')
  
class Event_Image(models.Model):
  event_table = models.ForeignKey(Event_Table, related_name='images', on_delete=models.CASCADE)  
  event_image_location = models.ImageField(upload_to='event/static', null = True, blank=True)  
  
  