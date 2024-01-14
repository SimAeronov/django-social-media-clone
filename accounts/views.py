from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SocioGhibliUserSignup(CreateView):
    form_class = forms.SocioGhibliUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')