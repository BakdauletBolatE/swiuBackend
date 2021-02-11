# Generated by Django 3.1.6 on 2021-02-11 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0004_auto_20210211_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название страницы')),
                ('content', models.TextField(verbose_name='Контентная часть')),
                ('img', models.ImageField(upload_to='Page/', verbose_name='Постер страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='PageImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='PageImages/', verbose_name='Фотографий страницы')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.page', verbose_name='pageImages')),
            ],
            options={
                'verbose_name': 'Фотограция страницы',
                'verbose_name_plural': 'Фотограций страницы',
            },
        ),
    ]