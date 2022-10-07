from django.contrib import admin
from blog.models import Post, Categories
from django.utils.safestring import mark_safe

# Register your models here.
# Яркий скин для административного интерфейса Django. https://django-grappelli.readthedocs.io/en/latest/quickstart.html


#admin.site.register(Categories)
# admin.site.register(Post)

@admin.register(Categories)
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
        'categories',
        'status',
        # 'publish',
        'slug',
        'reply',
    ]
    prepopulated_fields = {"slug": ("title",)} # автоматически предварительно заполнить поле SlugField
    list_filter = ('status', 'date_created', 'author') # список фильтр
    search_fields = ('title', 'content') # поля поиска
    list_display_links = ('id', 'title') # список отображаемых ссылок
    fields = ('title', 'slug', 'categories', 'content', 'photo', 'date_created',  'author', 'status',) # фильтр полей добовления постов
    date_hierarchy = 'date_created' # для быстрого перехода по иерархии дат
    # raw_id_fields = ('author',)
    list_editable = ('status', 'reply',) # список_ редактируемый
    # readonly_fields = ('date_created', 'get_html_photo') # для отображения только для чтения.

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50")

    get_html_photo.short_description = "Мініатюра"
