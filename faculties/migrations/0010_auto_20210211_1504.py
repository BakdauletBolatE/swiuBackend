# Generated by Django 3.1.6 on 2021-02-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0009_auto_20210211_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecategory',
            options={'verbose_name': 'Категория Страницы', 'verbose_name_plural': 'Категорий Страницы'},
        ),
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.CharField(default=1, max_length=255, verbose_name='Ссылка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]
