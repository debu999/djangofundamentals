import django

django.setup()
from gameplay.models import Move
from gameplay.models import Move, Game

from pprint import pprint as pp

pp(Game.objects.all())
g = Game.objects.get(pk=1)
pp(g.id)
g.status = "S"
g.save()
pp(Game.objects.get(pk=1).status)
pp(Game.objects.filter(status="F"))
pp(Game.objects.exclude(status="F"))
pp(Game.objects.filter(splayer__username="priyu12"))
g.move_set.all().delete()
m = Move(x=0, y=1, comments="First Move", byfirstplayer=False, game=g)
m.save()
pp(vars(m))
m1 = Move(x=1, y=0, comments="Second Move", byfirstplayer=True, game=g)
m1.save()
pp([m.game, g.move_set.all(), g.move_set.count(), g.move_set.exclude(comments="")])
