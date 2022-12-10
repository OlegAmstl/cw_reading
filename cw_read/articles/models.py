from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Создать статью'
        verbose_name_plural = 'Создать статьи'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
