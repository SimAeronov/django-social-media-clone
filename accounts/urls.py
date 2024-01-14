from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import SocioGhibliUserAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SocioGhibliUserSignup.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=SocioGhibliUserAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]