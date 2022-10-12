from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from django.utils.safestring import mark_safe
from blog.models import *

# Register your models here.
# Яркий скин для административного интерфейса Django. https://django-grappelli.readthedocs.io/en/latest/quickstart.html
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('id', 'name', 'parent', 'level', 'lft', 'rght', 'tree_id')
    list_display_links = ('id', 'name', 'parent',) # список отображаемых ссылок
    search_fields = ('name', 'parent',) # поля поиска
    prepopulated_fields = {"slug": ("name",)} # автоматически предварительно заполнить поле SlugField

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Post,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Post,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Супутні категорії (для цієї конкретної категорії)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Супутні категорії (в дереві)'

admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        # 'content',
        'get_html_photo',
        'date_created',
        'date_updated',
        'category',
        'status',
        # 'publish',
        'slug',
        'reply',
    ]
    prepopulated_fields = {"slug": ("title",)} # автоматически предварительно заполнить поле SlugField
    list_filter = ('status', 'date_created', 'author') # список фильтр
    search_fields = ('title', 'content') # поля поиска
    list_display_links = ('id', 'title') # список отображаемых ссылок
    fields = ('title', 'slug', 'category', 'content', 'photo', 'date_created',  'author', 'status',) # фильтр полей добовления постов
    date_hierarchy = 'date_created' # для быстрого перехода по иерархии дат
    # raw_id_fields = ('author',)
    list_editable = ('status', 'reply',) # список_ редактируемый
    # readonly_fields = ('date_created', 'get_html_photo') # для отображения только для чтения.

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 50")

    get_html_photo.short_description = "Мініатюра"


admin.site.register(Post, PageAdmin)
