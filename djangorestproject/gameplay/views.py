from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .models import Game, Move
from django import template
from .forms import InvitationModelForm

register = template.Library()


@register.filter(name='ifinlist')
def ifinlist(value, list):
    return True if value in list else False


@login_required(login_url="player_login")
def gamedetails(request):
    # gfp = Game.objects.filter(fplayer=request.user, status="F")
    # gsp = Game.objects.filter(splayer=request.user, status="S")
    # allmygames = list(gfp) + list(gsp)
    mygames = Game.objects.gamesforuser(request.user)
    activegames = mygames.active()
    context = {"ngames": Game.objects.count(),
               # "games": allmygames
               "games": mygames,
               "agames": activegames
               }
    return render(request, "gameplay/home.html", context=context)


# @login_required(login_url="player_login")
def welcome(request):
    if not request.user.is_authenticated:
        return redirect("player_login")
    else:
        context = dict()
        return render(request, "gameplay/welcome.html", context=context)


# @login_required(login_url="player_login")
def invite(request):
    if request.method == "POST":
        form = InvitationModelForm(request.POST)
    else:
        form = InvitationModelForm()
    context = {"form": form}
    return render(request, "gameplay/invite.html",
                  context=context)
