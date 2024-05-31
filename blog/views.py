from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import BlogForm
from blog.models import Blog

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class BlogListView(ListView):
    model = Blog
    template_name = "blog_app/blog_list.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog_app/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog_app/blog_form.html"
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog_app/blog_form.html"
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog_app/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
