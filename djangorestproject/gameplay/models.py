from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

GAME_STATUS_CHOICES = (
    ("F", "First Player To Move"),
    ("S", "Second Player To Move"),
    ("W", "First Player Wins"),
    ("L", "First Player Wins"),
    ("D", "Draw"),
)


class GameQuerySet(models.QuerySet):
    def gamesforuser(self, user):
        return self.filter(
            Q(fplayer=user) | Q(splayer=user))

    def active(self):
        return self.filter(
            Q(status="F") | Q(status="S"))


@python_2_unicode_compatible
class Game(models.Model):
    fplayer = models.ForeignKey(User, related_name="gamefirstplayer", on_delete=models.CASCADE)
    splayer = models.ForeignKey(User, related_name="gamesecondplayer", on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now_add=True)
    lastactive = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default="F", choices=GAME_STATUS_CHOICES)

    objects = GameQuerySet.as_manager()

    def __str__(self):
        return f"{self.fplayer} vs {self.splayer}"


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comments = models.CharField(max_length=300, blank=True)
    byfirstplayer = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.x}{self.y}"


class Invitation(models.Model):
    fuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitation_sent")
    tuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitation_received")
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fuser} requested {self.tuser} to" \
               f" play at {self.timestamp.strftime('%Y%m%d %H:%M:%S.%f')}"
