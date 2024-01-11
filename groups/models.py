from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
import misaka

current_user = get_user_model()
register = template.Library()


class SocioGhibliGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=False, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(current_user, through="SocioGhibliGroupMember")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["name"]

class SocioGhibliGroupMember(models.Model):
    group = models.ForeignKey(SocioGhibliGroup, related_name="memberships")
    user = models.ForeignKey(current_user, related_name="user_groups")
    favourite_quote = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ("group", "user")






