from django.contrib import admin

from .models import NationalLeague, RegionalLeague
# Register your models here.
admin.site.register(NationalLeague)
admin.site.register(RegionalLeague)

#retirer les groups de NationalLeague --> calculé automatiquement