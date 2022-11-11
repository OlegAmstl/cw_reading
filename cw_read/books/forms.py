from django.forms import (ModelForm,
                          TextInput,
                          ImageField,
                          NumberInput,
                          DateInput,
                          Textarea)
from django.contrib.auth import get_user_model

from .models import Book


User = get_user_model()


class AddBook(ModelForm):
    '''Форма добавления книги на портал.'''

    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'cover',
            'description',
            'pub_date',
            'num_pages',
            'genre',
        )

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание книги'
            }),
            'genre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр книги'
            }),
            'num_pages': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество страниц'
            }),
            'pub_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год издания'
            })
        }
