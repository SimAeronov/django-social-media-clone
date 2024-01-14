from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailInput, PasswordInput, ValidationError

from . import models



class SocioGhibliUserCreationForm(UserCreationForm):

    fav_ghibli_movie = CharField(max_length=100, required=True, widget=TextInput(attrs={'class': "form_input_field_custom"}))
    
    class Meta:
        model = models.SocioGhibliUser
        fields = ('username', 'email', 'password1', 'password2', 'fav_ghibli_movie',)
        widgets = {
            'username': TextInput(attrs={'class': 'form_input_field_custom'}),
            'email': EmailInput(attrs={'class': 'form_input_field_custom'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "First Name:" # This is the label that will be displayed in the form
        self.fields["email"].label = "Email:"
        self.fields["fav_ghibli_movie"].label = "My fav Ghibli movie:"
        self.fields["password1"].widget = PasswordInput(attrs={'class': 'form_input_field_custom'})
        self.fields["password2"].widget = PasswordInput(attrs={'class': 'form_input_field_custom'})


class SocioGhibliUserAuthenticationForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class': 'form_input_field_custom'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'form_input_field_custom'}))