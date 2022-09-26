from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from blog.views import *


urlpatterns = [
    # path('', cache_page(60)(UserListView.as_view()), name="user"),
    path('', BlogListView.as_view(), name="blog"),
    path('posts/user/<str:username>', UserListView.as_view(), name="user")
]
