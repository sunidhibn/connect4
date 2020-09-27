from django.db import models

# Create your models here.
def board_design():
    return [[""]*7]*6

class Game(models.Model):
    turn=models.IntegerField(default=1)
    board=models.JSONField(default=board_design)
    active=models.BooleanField(default=True)

    def save(self, *args, **kwargs):

        self.turn = 1 if self.turn==2 else 2
        super(Game, self ).save(*args, **kwargs)

class Audit(models.Model):
    game=models.IntegerField()
    player=models.IntegerField(default=0)
    old_state=models.JSONField(default=board_design)
    new_state=models.JSONField(default=board_design)
    time=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-time"]
