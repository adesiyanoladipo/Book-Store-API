# Generated by Django 3.2.8 on 2021-10-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Total_downloads',
            field=models.IntegerField(default=0),
        ),
    ]
