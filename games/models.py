from django.db import models

class games(models.Model):
    
    name_of_game = models.CharField(max_length=200)
    type_of_game = models.CharField(max_length=200)

class award_winners(models.Model):
       
       student_id = models.IntegerField()
       game_won_id = models.IntegerField()
       date = models.DateField()
       level = models.CharField(max_length=200)
       medal_type = models.CharField(max_length=200)
       achivements = models.CharField(max_length=200,null=True)
       
