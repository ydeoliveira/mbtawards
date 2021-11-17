from django.contrib import admin
from award.models import NationalLeagueAward, RegionalLeague, ChampionsLeague

# Register your models here.
admin.site.register(NationalLeagueAward)
admin.site.register(RegionalLeague)
admin.site.register(ChampionsLeague)