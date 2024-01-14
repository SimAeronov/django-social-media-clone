from django.contrib import admin
from . import models

@admin.register(models.SocioGhibliUser)
class SocioGhibliUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fav_ghibli_movie')

