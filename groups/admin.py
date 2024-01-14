from django.contrib import admin
from . import models

class SocioGhibliGroupMemberInline(admin.TabularInline):
    model = models.SocioGhibliGroupMember

@admin.register(models.SocioGhibliGroup)
class SocioGhibliGroupAdmin(admin.ModelAdmin):
    inlines = [SocioGhibliGroupMemberInline]

@admin.register(models.SocioGhibliGroupMember)
class SocioGhibliGroupMemberAdmin(admin.ModelAdmin):
    ordering = ("user__username",)
    def has_view_permission(self, request, obj=None):
        return False

    def has_edit_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

