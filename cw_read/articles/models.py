from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Article(models.Model):
    '''Модель для создания статьи.'''

    title = models.CharField(
        max_length=150,
         verbose_name='Название статьи'
         )
    text = models.TextField(
        verbose_name='Текст статьи'
        )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
        )
