from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post

# Create your views here.
class BlogHome(ListView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs): # Отображать контент по датам
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(context_def.items()))


    def get_queryset(self): # Отображать категории с аитором
        return Post.objects.filter(author=True).select_related('categoris')
