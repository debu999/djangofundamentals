from django.contrib import admin

# Register your models here.

from .models import Game, Move

# admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "fplayer", "splayer", "status")
    list_editable = ("status", )

#
# admin.site.register(Move)

@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ("mvdet", "x", "y", "comment", "byfirstplayer", "movetime")
    list_editable = ("comment", )

    def mvdet(self, obj):
        return str(obj)
    mvdet.short_description = "Move Details"