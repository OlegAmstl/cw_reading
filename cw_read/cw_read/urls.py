from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ] 
