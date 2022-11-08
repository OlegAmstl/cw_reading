# Generated by Django 4.1.2 on 2022-11-04 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название книги')),
                ('author', models.CharField(max_length=150, verbose_name='Автор книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('cover', models.ImageField(upload_to='', verbose_name='Обложка книги')),
                ('genre', models.CharField(max_length=150, verbose_name='Жанр книги')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
                ('num_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('add_date', models.DateTimeField(verbose_name='Дата добавления книги на сайт')),
                ('user_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]