from time import timezone
from django.db import models
# https://docs.djangoproject.com/en/4.1/ref/urlresolvers/
from django.urls import reverse
# https://docs.djangoproject.com/en/4.1/topics/auth/default/
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
# https://docs.djangoproject.com/en/4.1/topics/db/models/
# https://django.fun/ru/docs/django/4.0/topics/db/models/


class Categoris(models.Model):
    # поля модели
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорія") # настройка полей
    category_slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")

    # мета опция
    class Meta:
        verbose_name = ("Категорія")
        verbose_name_plural = ("Категорії")

    # методы модели
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Categoris_detail", kwargs={"categoris_slug": self.slug})


class Post(models.Model):
    # поля модели
    title = models.CharField(("Назва"), max_length=100,  db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")
    # content = models.TextField("Текст статті", max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Час публікації")
    date_updated= models.DateTimeField(auto_now=True, verbose_name="Час зміни")
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # categoris = models.ForeignKey(Categoris, on_delete=models.CASCADE, verbose_name="Категорії")

    # мета опция
    class Meta:
        verbose_name = ("Пост")
        verbose_name_plural = ("Пости")

    # методы модели
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"slug": self.slug})
