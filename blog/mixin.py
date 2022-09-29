from django.urls import reverse_lazy
from blog.models import Post, Categoris


class UserMixin:
    # Выбор пользователя
    pass


class UserPostFormMixin:
    # Ограничение user в полях и формах
    # Перенапровление не посты user
    model = Post
    fields = ['title', 'content']
    succes_url_redirect = reverse_lazy('user')
