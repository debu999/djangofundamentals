from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *


class InvitationModelForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ("fuser", "timestamp")

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)


class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = []

    def clean(self):
        x = self.cleaned_data.get("x")
        y = self.cleaned_data.get("y")
        game = self.instance.game

        try:
            if game.board()[y][x] is not None:
                raise ValidationError("Square is not Empty")
        except IndexError as ierr:
            raise ValidationError("Invalid Coordinates")
        return self.cleaned_data
