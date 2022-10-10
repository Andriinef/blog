from django.urls import path, include, re_path
from django.contrib.auth.views import PasswordResetView
from blog.views import *


urlpatterns = [
    # path('', cache_page(60)(UserListView.as_view()), name="user"),
    path('', BlogListView.as_view(), name="blog"),
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/
    path('password_reset_user/', PasswordResetView.as_view(template_name = 'registration/password_reset_user.html'), name="password_reset_user"),
    path('auth/', include('django.contrib.auth.urls')), # аутентификация пользователя от django
    path('post/<slug:post_slug>/', PostDetailViev.as_view(), name="post"),
    path('user/AnonymousUser/', AnonymousUserListView.as_view(), name="anonymous"),
    path('user/<str:username>/', UserListView.as_view(), name="user"),
    path('category/<slug:category_slug>/', CategoriesListView.as_view(), name="category"),
    path('register/', RegisterViev.as_view(), name="register"),
]
