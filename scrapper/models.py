from django.db import models


# Create your models here.
class PlayerGoalScore(models.Model):
    rank = models.IntegerField()
    player_name = models.CharField(max_length=255)
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    minutes_played = models.IntegerField()
    matches_played = models.IntegerField()
    penalties_scored = models.IntegerField()
    goals_left_foot = models.IntegerField()
    goals_right_foot = models.IntegerField()
    headed_goals = models.IntegerField()
