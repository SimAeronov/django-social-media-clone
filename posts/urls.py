from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.SocioGhibliPostList.as_view(), name="all"),
    path("new/", views.SocioGhibliCreatePost.as_view(), name="create"),
    path("by/<username>",views.SocioGhibliUserPosts.as_view(), name="for_user"),
    path("by/<username>/<int:pk>/", views.SocioGhibliPostDetail.as_view(), name="single"),
    path("delete/<int:pk>/", views.SocioGhibliDeletePost.as_view(), name="delete")
]