from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreatingForm


class SignUp(CreateView):
    '''View для страницы регистрации полдьзователя.'''

    form_class = CreatingForm
    success_url = reverse_lazy('books:index')
    template_name = 'users/signup.html'
