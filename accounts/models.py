from django.db import models
from django.contrib import auth

# Simonko models here.
class SocioGhibliUser(auth.models.User, auth.models.PermissionsMixin):
    fav_ghibli_movie = models.CharField(max_length=100)
    def __str__(self):
        return "@{}".format(self.username)
