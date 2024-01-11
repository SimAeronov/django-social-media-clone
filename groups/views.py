from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import SocioGhibliGroup, SocioGhibliGroupMember

class CreateSocioGhibliGroupView(LoginRequiredMixin, CreateView):
    fields = ("name", "description")
    model = SocioGhibliGroup
    template_name = "groups/group_form.html"

class SingleSocioGhibliGroupView(DetailView):
    model = SocioGhibliGroup
    context_object_name = "group"
    temmplate_name = "groups/group_detail.html"

class ListSocioGhibliGroupView(ListView):
    model = SocioGhibliGroup
    template_name = "groups/group_list.html"
