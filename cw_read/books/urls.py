from django.urls import path

from .views import index, book_add, book_detail

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    path('add_book/', book_add, name='add_book'),
    path('books/<int:pk>', book_detail, name='book_detail')
]
