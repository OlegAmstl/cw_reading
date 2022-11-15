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
        verbose_name="Обложка книги",
        upload_to="books/",
        blank=True
    )
    genre = models.CharField(
        max_length=150,
        verbose_name="Жанр книги"
    )
    pub_date = models.CharField(
        max_length=50,
        verbose_name="Дата публикации"
    )
    num_pages = models.IntegerField(
        verbose_name="Количество страниц",
        blank=True
    )
    add_date = models.DateTimeField(
        verbose_name="Дата добавления книги на сайт",
        auto_now=True
    )
    user_site = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='books',
        on_delete=models.CASCADE,
    )
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    class BooksReadBase(models.Model):
        user = models.ForeignKey(User,
                                 verbose_name='Пользователь',
                                 on_delete=models.CASCADE)

        class Meta:
            abstract = True

        def __str__(self):
            return self.user.username

    class AddReadBook(BooksReadBase):
        class Meta:
            db_table = ''
