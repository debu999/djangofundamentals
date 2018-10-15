from django.forms import ModelForm

from .models import *


class InvitationModelForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ("fuser", "timestamp")
