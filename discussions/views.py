from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from blog.models import Post, Categories


# Create your views here.

class DiscussionsListView(ListView):
    model = Post
    template_name = ".html"
