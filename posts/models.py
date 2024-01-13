from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

import misaka
from groups.models import SocioGhibliGroup

current_user = get_user_model()

class SocioGhibliPost(models.Model):
    user = models.ForeignKey(current_user, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(SocioGhibliGroup, related_name="posts", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username, "pk": self.pk})
    
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]


