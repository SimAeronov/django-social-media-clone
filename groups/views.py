from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.contrib import messages
from django.db import IntegrityError
from .models import SocioGhibliGroup, SocioGhibliGroupMember
from .forms import SocioGhibliGroupForm

class CreateSocioGhibliGroupView(LoginRequiredMixin, CreateView):
    form_class = SocioGhibliGroupForm
    model = SocioGhibliGroup
    template_name = "groups/group_form.html"

class SingleSocioGhibliGroupView(DetailView):
    model = SocioGhibliGroup
    context_object_name = "group"
    template_name  = "groups/group_detail.html"

class ListSocioGhibliGroupView(ListView):
    model = SocioGhibliGroup
    template_name = "groups/group_list.html"

class JoinSocioGhibliGroupView(LoginRequiredMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(SocioGhibliGroup, slug=self.kwargs.get("slug"))
        try:
            SocioGhibliGroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, "Warning, already a member!")
        else:
            messages.success(self.request, "You are now a member!")
        
        return super().get(request, *args, **kwargs)

class LeaveSocioGhibliGroupView(LoginRequiredMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})
    
    def get(self, request, *args, **kwargs):
        try:
            membership = SocioGhibliGroupMember.objects.filter(
                user = self.request.user,
                group__slug = self.kwargs.get("slug")
            ).get()
        except SocioGhibliGroupMember.DoesNotExists:
            messages.warning(self.request, "Sorry you are not in this group!")
        else:
            membership.delete()
            messages.success(self.request, "You have left the group!")
        return super().get(request, *args, **kwargs)