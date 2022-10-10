from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from blog.models import Post, Categories
from blog.forms import UserCreationForm

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
    ordering = ['-date_created']
    paginate_by = 2

    # Возвращаем контекстные данные для отображения списка объектов.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # queryset = Post.objects.filter(status=True)
        # context['blog_home'] = queryset.order_by('-date_created', '-id')
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
    ordering = ['-date_created']
    paginate_by = 3

    # Возвращаем контекстные данные для отображения списка объектов.
    # Выборка отображения постов от конкретного user(author) через queryset
    # Переопределение модель_имя в данном варианте на ['blog_post_user_list']
    # Cортировка по дате публикации начиная с последней с помощью order_by
    """ https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/ """

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # queryset = Post.objects.filter(author=user, status=True)
        # context['blog_post_user_list'] = queryset.order_by('-date_created', '-id')
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


class CategoriesListView(ListView):
    model = Categories
    template_name = "categories_list.html"
    context_object_name = 'list_categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterViev(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form' : UserCreationForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # password2 = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password,)
            login(request, user)
            return redirect('blog')
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

class AnonymousUserListView(ListView):
    model = Post
    template_name = "blog/anonymous.html"
