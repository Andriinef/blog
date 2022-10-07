from enum import unique
from random import choices
from time import timezone
from django.db import models
# https://docs.djangoproject.com/en/4.1/ref/urlresolvers/
from django.urls import reverse
# https://docs.djangoproject.com/en/4.1/topics/auth/default/
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
# https://docs.djangoproject.com/en/4.1/topics/db/models/
# https://django.fun/ru/docs/django/4.0/topics/db/models/


class Categories(models.Model):
    # поля модели
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорія") # настройка полей
    category_slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")

    # Модель поста для расширения или изменения доступа к модели
    # мета опция
    class Meta:
        verbose_name = ("Категорія")
        verbose_name_plural = ("Категорії")

    # методы модели
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.category_slug})


class Post(models.Model):
    # поля модели
    title = models.CharField("Назва", max_length=100,  db_index=True) # Настройки полей
    slug = models.SlugField(max_length=150, unique_for_date='publish', unique=True, db_index=True, verbose_name="URL")
    # content = models.TextField("Текст статті", max_length=5000, blank=True, null=True)
    content = RichTextField("Текст статті", blank=True, null=True) # ckeditor
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Фото")
    publish = models.DateField(auto_now = False, auto_now_add = True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Час публікації")
    date_updated= models.DateTimeField(auto_now=True, verbose_name="Час зміни")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    status = models.BooleanField(default=True, verbose_name="Публікація")
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='postcategory', verbose_name="Категорії")
    likes = models.ManyToManyField(User, related_name='postcomment',verbose_name="Лайки", blank=True)
    reply = models.ForeignKey("self", related_name='reply_ok',verbose_name="Відповідь", on_delete=models.CASCADE, null=True, blank=True)

    # Модель поста для расширения или изменения доступа к модели
    # мета опция
    class Meta:
        verbose_name = ("Пост")
        verbose_name_plural = ("Пости")

    # методы модели
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # Подсчет лайков
    def total_likes(self):
        return self.likes.count()
