from django.contrib import admin
from blog.models import Post, Categoris
from django.utils.safestring import mark_safe

# Register your models here.
# Яркий скин для административного интерфейса Django. https://django-grappelli.readthedocs.io/en/latest/quickstart.html


#admin.site.register(Categoris)
# admin.site.register(Post)

@admin.register(Categoris)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name') # список отображаемых ссылок
    search_fields = ('name',) # поля поиска
    prepopulated_fields = {"category_slug": ("name",)} # автоматически предварительно заполнить поле SlugField


@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        # 'content',
        'get_html_photo',
        'date_created',
        'date_updated',
        'categoris',
        'slug',
        'reply',
    ]
    prepopulated_fields = {"slug": ("title",)} # автоматически предварительно заполнить поле SlugField
    search_fields = ('title', 'content') # поля поиска
    list_display_links = ('id', 'title') # список отображаемых ссылок
    fields = ('title', 'slug', 'categoris', 'content', 'photo', 'date_created', 'likes', 'reply','author',) # поля
    # list_editable = ('is_published',) # список_ редактируемый
    # list_filter = ('is_published', 'date_created') # список фильтр
    # readonly_fields = ('date_created', 'date_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50")

    get_html_photo.short_description = "Мініатюра"
