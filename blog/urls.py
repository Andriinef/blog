from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    # path('', cache_page(60)(BlogListView.as_view()), name="blog"),
    path('',BlogListView.as_view(), name="blog"),
]
