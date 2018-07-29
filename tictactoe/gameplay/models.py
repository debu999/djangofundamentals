from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
import pytz

from datetime import datetime

sgtz = pytz.timezone("Asia/Singapore")

GAME_STATUS_CHOICES = (
    ('F', 'First Player To Move'),
    ('S', 'Second Player To Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'),
)

class GamesQuerySet(models.QuerySet):
    def gameforuser(self, user):
        return self.filter(
            Q(fplayer=user) | Q(splayer=user)
        )

    def active(self):
        return self.filter(
            Q(status="F") | Q(status="S")
        )


@python_2_unicode_compatible
class Game(models.Model):
    fplayer = models.ForeignKey(User, related_name="gamefplayer", on_delete=models.CASCADE)
    splayer = models.ForeignKey(User, related_name="gamesplayer", on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now_add=True)
    lastactive = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)
    objects = GamesQuerySet.as_manager()

    def __str__(self):
        return "{} vs {}".format(self.fplayer, self.splayer)




class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=500, blank=True)
    byfirstplayer = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="gm")
    movetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Move by {} at location {}{}".format(self.game.fplayer.username if self.byfirstplayer
                                                    else self.game.splayer.username, self.x, self.y)

