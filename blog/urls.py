from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from blog.views import *


urlpatterns = [
    # path('', cache_page(60)(UserListView.as_view()), name="user"),
    path('', BlogListView.as_view(), name="blog"),
    path('post/<slug:post_slug>/', PostDetailViev.as_view(), name="post"),
    path('user/<str:username>/', UserListView.as_view(), name="user"),
]
