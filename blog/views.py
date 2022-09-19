"""Views for Blog App"""
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import PostForm
from .models import Post

class PostCreate(CreateView):
    """Create new blog posts"""

    form_class = PostForm
    model = Post
    template_name = "post/form.html"
    extra_context = {"update": False}


class PostDetail(DetailView):
    """Display a single blog Post"""
    model = Post
    template_name = "post/detail.html"


class PostDelete(
    DeleteView
):
    """Delete a single blog post"""
    model = Post
    template_name = "post/confirm_delete.html"
    success_url = reverse_lazy("post_list")


class PostList(ListView):
    """Display a list of blog Posts"""

    model = Post
    template_name = "post/list.html"


class PostUpdate(UpdateView
):
    """Update existing blog posts"""
    model = Post
    form_class = PostForm
    template_name = "post/form.html"
    extra_context = {"update": True}