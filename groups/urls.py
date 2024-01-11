from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "groups"

urlpatterns = [
    path("", views.ListSocioGhibliGroupView.as_view(), name="all"),
    path("new/", views.CreateSocioGhibliGroupView.as_view(), name="create"),
    path("posts/in/<slug>/", views.SingleSocioGhibliGroupView.as_view(), name="single"),
]