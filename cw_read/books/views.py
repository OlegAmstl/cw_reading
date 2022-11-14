from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import AddBook


def index(request):
    books = Book.objects.order_by('-add_date')[:5]
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context=context)


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


def book_detail(request, pk):
    template = 'books/book_detail.html'
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, template, context=context)
