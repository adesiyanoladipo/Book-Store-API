# Generated by Django 3.2.8 on 2021-10-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='Wuthering Height', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default='2000'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(default='This books are all dope'),
            preserve_default=False,
        ),
    ]
