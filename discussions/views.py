from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy

from discussions.forms import ContactForm

# Create your views here.

class DiscussionsListView(ListView):
    pass

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'discussions/contact_email.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('blog')
