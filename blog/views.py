from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.models import User

from blog.models import Post, Categories

# Create your views here.


class BlogListView(ListView):
    """ Главная страница """
    """ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/ """
    # Модель Post в moddel.py
    model = Post
    # Имя шаблона html
    template_name = "blog/home.html"
    # object, model_post, наш вариант =
    # представление_модель_имя
    context_object_name = "blog_home"
    paginate_by = 3

    # Возвращаем контекстные данные для отображения списка объектов.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Post.objects.filter(status=True)
        context['blog_home'] = queryset.order_by('-date_created')
        return context


class UserListView(ListView):
    """ Список постов от user """
    """ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/ """
    # Модель Post в moddel.py
    model = Post
    # Имя шаблона html
    template_name = "blog/user_post.html"
    # object, model_post, наш вариант =
    # представление_модель_имя
    context_object_name = "blog_post_user_list"
    paginate_by = 3

    # Возвращаем контекстные данные для отображения списка объектов.
    # Выборка отображения постов от конкретного user(author) через queryset
    # Переопределение модель_имя в данном варианте на ['blog_post_user_list']
    # Cортировка по дате публикации начиная с последней с помощью order_by
    """ https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/ """

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)
        context['blog_post_user_list'] = queryset.order_by('-date_created')
        return context

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')


class PostDetailViev(DetailView):
    """ Полное описание поста от user """
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AnonymousUserListView(ListView):
    model = Post
    template_name = "blog/anonymous.html"


class CategoriesListView(ListView):
    model = Categories
    template_name = "categories_list.html"
    context_object_name = 'list_categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
