from django.contrib import admin

from .models import season,club,player,fixture


# Register your models here.

admin.site.register(season)
admin.site.register(club)
admin.site.register(player)
admin.site.register(fixture)
