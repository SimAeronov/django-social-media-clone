from django import forms
from .models import SocioGhibliPost

class SocioGhibliCreatePostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = SocioGhibliPost
        widgets ={
            "message": forms.Textarea(attrs={"class": "form_input_field_custom list-group-item"}),
            "group": forms.Select(attrs={"class": "form_input_field_custom list-group-item"})
        }