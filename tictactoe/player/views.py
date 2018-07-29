from django.shortcuts import render

# Create your views here.
from gameplay.models import Game


def home(request):
    mygames = Game.objects.gameforuser(request.user)
    acgames = Game.objects.active()
    # gfp = Game.objects.filter(fplayer=request.user, status="F")
    # gsp = Game.objects.filter(splayer=request.user, status="S")
    # return render(request, "player/home.html", {"ngames": Game.objects.count()})
    # allmygames = sorted(list(gfp) + list(gsp), key=lambda game: game.id)
    return render(request, "player/home.html", {"games": acgames})