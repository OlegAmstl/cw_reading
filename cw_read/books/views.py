from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import AddBook


def index(request):
    books = Book.objects.order_by('-add_date')[:5]
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context=context)

#
# class AddBookView(CreateView):
#     '''View для отображения страницы добавления новой книги на портал.'''
#
#     form_class = AddBook
#     success_url = reverse_lazy('books:index')
#     template_name = 'books/add_book.html'
@login_required
def book_add(request):
    '''Добавление новой книги на сайт.'''
    err = ''
    if request.method == 'POST':
        form = AddBook(request.POST, files=request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user_site = request.user
            form.save()
            return redirect('books:index')
        else:
            err = 'Форма была неверной'
    template = 'books/add_book.html'
    form = AddBook
    context = {
        'form': form,
        'err': err
    }

    return render(request, template, context=context)
