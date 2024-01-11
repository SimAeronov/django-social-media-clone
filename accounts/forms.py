from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField



class SocioGhibliUserCreationForm(UserCreationForm):

    fav_ghibli_movie = CharField(max_length=100, required=True)
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields["username"].label = "First Name:" # This is the label that will be displayed in the form
        self.fields["email"].label = "Email:"
        self.fields["fav_ghibli_movie"].label = "My fav Ghibli movie:"
