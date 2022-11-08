from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls'))
]
