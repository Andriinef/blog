from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from discussions.views import *


urlpatterns = [
    path('discussions/', DiscussionsListView.as_view(), name="discussions"),
]
