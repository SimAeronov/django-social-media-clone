from django import forms
from . import models

class SocioGhibliGroupForm(forms.ModelForm):
    class Meta:
        model = models.SocioGhibliGroup
        fields = ("name", "description")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form_input_field_custom list-group-item"}),
            "description": forms.Textarea(attrs={"class": "form_input_field_custom list-group-item"}),
        }