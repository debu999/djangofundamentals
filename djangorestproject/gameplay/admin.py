from django.contrib import admin

# Register your models here.

from .models import Game, Move


# admin.site.register(Move)
# admin.site.register(Game)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "fplayer", "splayer", "status")
    list_editable = ("status",)


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ("id", "x", "y", "comments", "byfirstplayer", "game")
    list_editable = ("x", "y", "comments")
