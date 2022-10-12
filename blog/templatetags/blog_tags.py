from django import template
from blog.models import *

# https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/
register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()
