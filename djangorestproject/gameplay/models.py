from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.urls import reverse

GAME_STATUS_CHOICES = (
    ("F", "First Player To Move"),
    ("S", "Second Player To Move"),
    ("W", "First Player Wins"),
    ("L", "First Player Wins"),
    ("D", "Draw"),
)

BOARD_SIZE = 3


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

    def get_absolute_url(self):
        return reverse("gameplay_detail", args=[self.id])

    def __str__(self):
        return f"{self.fplayer} vs {self.splayer}"

    def board(self):
        """Return a 2d list of Move Objects so you can get the
        state of a square at position [y][x]."""
        board = [[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for mv in self.move_set.all():
            board[mv.y][mv.x] = mv

        return board

    def isusermove(self, user):
        return (user == self.fplayer and self.status == "F") or \
               (user == self.splayer and self.status == "S")

    def newmove(self):
        if self.status not in "FS":
            raise ValueError("Cannot make move in Completed Games.")

        return Move(game=self,
                    byfirstplayer=self.status == "F")

    def updateaftermove(self, move):
        self.status = self._getgamestatusaftermove(move)

    def _getgamestatusaftermove(self, move):
        x, y = move.x, move.y
        board = self.board()
        if ((board[y][0] == board[y][1] == board[y][2] and board[y][0] is not None) or \
                (board[0][x] == board[1][x] == board[2][x] and board[0][x] is not None) or \
                (board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None) or \
                (board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None)):
            return "W" if move.byfirstplayer else "L"
        if self.move_set.count() >= BOARD_SIZE ** 2:
            return "D"
        return "S" if self.status == "F" else "F"


class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE - 1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE - 1)])
    comments = models.CharField(max_length=300, blank=True)
    byfirstplayer = models.BooleanField(editable=False)

    game = models.ForeignKey(Game, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return f"{self.x}{self.y}"

    def __eq__(self, other):
        if other is None:
            return False
        return other.byfirstplayer == self.byfirstplayer

    def save(self, *args, **kwargs):
        super(Move, self).save(*args, **kwargs)
        self.game.updateaftermove(self)
        self.game.save()


class Invitation(models.Model):
    fuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitation_sent")
    tuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitation_received",
                              verbose_name="User to Invite",
                              help_text="Please select the user you want to play game with.")
    message = models.CharField(max_length=300,
                               blank=True,
                               verbose_name="Optional Message",
                               help_text="Its always good to add a friendly message.")

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fuser} requested {self.tuser} to" \
               f" play at {self.timestamp.strftime('%Y%m%d %H:%M:%S.%f')}"
