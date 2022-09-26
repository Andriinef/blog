from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from blog.models import Post

# Create your views here.


class BlogListView(ListView):
    pass


class UserListView(ListView):
    # Модель Post в moddel.py
    model = Post
    # Имя шаблона html
    template_name = "blog/user_post.html"
    # object, model_post, наш вариант =
    # представление_модель_имя
    context_object_name = "blog_post_user_list"
    paginate_by = 6

    # Выборка отображения
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')
