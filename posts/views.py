from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms

current_user = get_user_model()

class SocioGhibliPostList(SelectRelatedMixin, ListView):
    model = models.SocioGhibliPost
    select_related = ("user", "group")

class SocioGhibliUserPosts(ListView):
    model = models.SocioGhibliPost
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post.user = current_user.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get("username"))
        except current_user.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class SocioGhibliPostDetail(SelectRelatedMixin, DetailView):
    models = models.SocioGhibliPost
    select_related = ["user", "group"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))

class SocioGhibliCreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ("message", "group")
    model = models.SocioGhibliPost

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SocioGhibliDeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.SocioGhibliPost
    select_related = ("user", "group")
    success_url = reverse_lazy("post:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
       



