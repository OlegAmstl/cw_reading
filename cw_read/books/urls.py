from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, book_add

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    path('add_book/', book_add, name='add_book')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
