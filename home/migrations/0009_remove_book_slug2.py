# Generated by Django 3.2.8 on 2021-10-21 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_book_slug2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug2',
        ),
    ]
