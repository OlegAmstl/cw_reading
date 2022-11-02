from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    """Модель книги."""

    title = models.CharField(
        max_length=150,
        verbose_name="Название книги"
    )
    author = models.CharField(
        max_length=150,
        verbose_name="Автор книги"
    )
    description = models.TextField(
        verbose_name="Описание книги"
    )
    cover = models.ImageField(
        verbose_name="Обложка книги"
    )
    genre = models.CharField(
        max_length=150,
        verbose_name="Жанр книги"
    )
    pub_date = models.DateField(
        verbose_name="Дата публикации"
    )
    num_pages = models.IntegerField(
        verbose_name="Количество страниц"
    )
    add_date = models.DateTimeField(
        verbose_name="Дата добавления книги на сайт"
    )
    user_site = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='books'
    )
