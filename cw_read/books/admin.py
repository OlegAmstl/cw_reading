from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    '''Модель Book для админки.'''

    list_display = (
        'title',
        'author',
        'genre',
        'pub_date',
        'add_date',
        'user_site'
    )
    list_filter = (
        'title',
        'author',
        'user_site'
    )
    search_fields = (
        'title',
        'author',
    )
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)
