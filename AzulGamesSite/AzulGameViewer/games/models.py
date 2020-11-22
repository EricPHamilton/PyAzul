from django.db import models

# Create your models here.
class Game(models.Model):
    game_time = models.CharField('game_time', max_length=100)

class Turn(models.Model):
    game_id = models.ForeignKey(Game, related_name='turns', on_delete=models.CASCADE)
    turn_ctr = models.IntegerField('turn_ctr')
    board_state = models.JSONField()
    turn_string = models.CharField('turn_string', max_length=200)
