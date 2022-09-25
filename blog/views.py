from gc import get_objects
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from blog.models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = "templates/blog/blog.html"
    context_object_name = "posts"
    ordering = ['-date_created']
    paginate_by = 6

    # Отображать контент по датам
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(BlogListView), self.get_context_data(**kwargs)
    #     context_def = self.get_user_context(title="Головна сторінка")
    #     return dict(list(context.items()) + list(context_def.items()))

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')
