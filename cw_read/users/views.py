from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreatingForm
from books.models import User, Book
from .models import Follow


class SignUp(CreateView):
    '''View для страницы регистрации полдьзователя.'''

    form_class = CreatingForm
    success_url = reverse_lazy('books:index')
    template_name = 'users/signup.html'


def profile(request, username):
    template = 'users/profile.html'
    author = get_object_or_404(User, username=username)
    user = request.user
    read_bboks = Book.objects.filter(user_site=user).count()
    following = False
    if user.is_authenticated:
        if Follow.objects.filter(user=user, author=author).exists():
            following=True
    context = {
        'read_books': read_bboks,
        'author': author,
        'user': user,
        'following': following
    }
    return render(request, template, context=context)
