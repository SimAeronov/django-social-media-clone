from django.contrib import admin
from . import models


@admin.register(models.SocioGhibliPost)
class SocioGhibliPostAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)