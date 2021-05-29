# Generated by Django 3.1.6 on 2021-05-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, verbose_name='Год')),
                ('year_ru', models.IntegerField(default=0, null=True, verbose_name='Год')),
                ('year_en', models.IntegerField(default=0, null=True, verbose_name='Год')),
                ('year_kk', models.IntegerField(default=0, null=True, verbose_name='Год')),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(upload_to='Year/Posters/')),
            ],
            options={
                'verbose_name': 'Год для Библиотеки',
                'verbose_name_plural': 'Год для Библиотеки',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Фио')),
                ('group', models.CharField(blank=True, max_length=255, null=True, verbose_name='Группа')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('course', models.CharField(blank=True, max_length=255, null=True, verbose_name='Курс')),
                ('op', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.educationalprograms')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.registrationcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название книги')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название книги')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название книги')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание книги')),
                ('description_en', models.TextField(null=True, verbose_name='Описание книги')),
                ('description_kk', models.TextField(null=True, verbose_name='Описание книги')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='Book/Posters/')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Book/Posters/')),
                ('pdffile', models.FileField(blank=True, null=True, upload_to='Book/Pdf')),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('eduProgram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.educationalprograms')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.year')),
            ],
            options={
                'verbose_name': 'Библиотека',
                'verbose_name_plural': 'Библиотеки',
            },
        ),
    ]
