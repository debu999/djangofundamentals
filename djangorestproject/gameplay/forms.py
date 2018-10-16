from django.forms import ModelForm

from .models import *


class InvitationModelForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ("fuser", "timestamp")

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
