# Generated by Django 4.1.2 on 2022-11-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]