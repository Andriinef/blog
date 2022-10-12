from django import forms
from blog.models import *
# from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label="Iм'я", max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={"cols": 60, "rows": 10}))
    # captcha = CaptchaField()


# class UserPostForm(forms.ModelForm):

#     class Meta:
#          fields = ('title', 'slug', 'categories', 'content', 'photo', 'date_created',  'author', 'status',) # фильтр полей добовления постов
