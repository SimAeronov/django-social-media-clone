from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import Http404
from braces.views import SelectRelatedMixin
from posts.models import SocioGhibliPost
from . import models
from . import forms

current_user = get_user_model()

class SocioGhibliPostList(SelectRelatedMixin, ListView):
    model = models.SocioGhibliPost
    select_related = ("user", "group")
    template_name = "posts/post_list.html"

class SocioGhibliUserPosts(ListView):
    model = models.SocioGhibliPost
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            user_instance = current_user.objects.get(username__iexact=self.kwargs.get("username"))
            self.post_user = SocioGhibliPost.objects.filter(user=user_instance).order_by('-created_at')
        except current_user.DoesNotExist:
            raise Http404
        else:
            return self.post_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class SocioGhibliPostDetail(SelectRelatedMixin, DetailView):
    model = models.SocioGhibliPost
    select_related = ["user", "group"]
    queryset = model.objects.select_related("user", "group")
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return self.queryset.filter(user__username__iexact=self.kwargs.get("username"))

class SocioGhibliCreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ("message", "group")
    model = models.SocioGhibliPost
    template_name = "posts/post_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SocioGhibliDeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.SocioGhibliPost
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")
    template_name = "posts/post_confirm_delete.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
       



