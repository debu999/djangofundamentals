from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Game, Move
from django import template
from .forms import InvitationModelForm, MoveForm
from .models import Invitation

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
    finishedgames = mygames.difference(activegames)
    invitations = request.user.invitation_received.all()
    context = {"ngames": Game.objects.count(),
               # "games": allmygames
               "games": mygames,
               "agames": activegames,
               "invitations": invitations,
               "finishedgames": finishedgames
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
        invitation = Invitation(fuser=request.user)
        form = InvitationModelForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = InvitationModelForm()
    context = {"form": form}

    return render(request, "gameplay/invite.html",
                  context=context)


@login_required(login_url="player_login")
def acceptinvitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.tuser:
        raise PermissionDenied

    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                fplayer=invitation.fuser,
                splayer=invitation.tuser,
            )
        invitation.delete()
        # return redirect("gamedetails")
        return redirect(game)
    else:
        return render(request, "gameplay/acceptinvitation.html",
                      {"invitation": invitation})


@login_required(login_url="player_login")
def gamedetail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {"game": game}
    print(vars(game))
    if game.isusermove(request.user):
        context["form"] = MoveForm()
    return render(request, "gameplay/gamedetail.html", context=context)


@login_required(login_url="player_login")
def makemove(request, id):
    game = get_object_or_404(Game, pk=id)
    if not game.isusermove(request.user):
        raise PermissionDenied
    move = game.newmove()
    form = MoveForm(instance=move, data=request.POST)
    if form.is_valid():
        move.save()
        return redirect("gameplay_detail", id)
    else:
        context = {"game": game, "form": form}
        return render(request, "gameplay/gamedetail.html", context=context)
