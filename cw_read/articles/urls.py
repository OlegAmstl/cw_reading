from django.urls import path
from .views import all_articles

app_name = 'articles'

urlpatterns = [
    path('', all_articles, name='all_articles')
]
