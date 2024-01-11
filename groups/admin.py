from django.contrib import admin
from . import models

class SocioGhibliGroupMemberInline(admin.TabularInline):
    model = models.SocioGhibliGroupMember

admin.register(models.SocioGhibliGroup)