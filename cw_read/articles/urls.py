from django.urls import path
from .views import all_articles, create_article

app_name = 'articles'

urlpatterns = [
    path('', all_articles, name='all_articles'),
    path('create_article/', create_article, name='create_article')
]
