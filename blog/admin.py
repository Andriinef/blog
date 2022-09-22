from django.contrib import admin
from blog.models import Post, Categoris

# Register your models here.
# Яркий скин для административного интерфейса Django. https://django-grappelli.readthedocs.io/en/latest/quickstart.html


admin.site.register(Categoris)


@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        # 'content',
        # 'author',
        # 'categoris',
    ]
