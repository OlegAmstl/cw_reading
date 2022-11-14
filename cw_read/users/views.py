from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreatingForm


class SignUp(CreateView):
    '''View для страницы регистрации полдьзователя.'''

    form_class = CreatingForm
    success_url = reverse_lazy('books:index')
    template_name = 'users/signup.html'


def profile(request, username):
    template = 'users/profile.html'
    userrr = get_object_or_404(U)
