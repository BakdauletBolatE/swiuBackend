# Generated by Django 3.1.6 on 2021-05-29 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Должность персонала')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Должность персонала')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Должность персонала')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='Должность персонала')),
                ('slug', models.SlugField(unique=True, verbose_name='Url Должность персонала')),
            ],
            options={
                'verbose_name': 'Должность персонала',
                'verbose_name_plural': 'Должность персоналов',
            },
        ),
        migrations.CreateModel(
            name='StaffCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория персонала')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Категория персонала')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Категория персонала')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='Категория персонала')),
                ('slug', models.SlugField(unique=True, verbose_name='Url Категория персонала')),
            ],
            options={
                'verbose_name': 'Категория персонала',
                'verbose_name_plural': 'Категорий персонала',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Филтрация')),
                ('name', models.CharField(max_length=255, verbose_name='Имя персонала')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Имя персонала')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Имя персонала')),
                ('name_kk', models.CharField(max_length=255, null=True, verbose_name='Имя персонала')),
                ('slug', models.SlugField(unique=True, verbose_name='Url персонала')),
                ('img', models.ImageField(upload_to='Staff/Posters', verbose_name='Изоброжения персонала')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта персонала')),
                ('adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес персонала')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон персонала')),
                ('about', models.TextField(verbose_name='О персонале')),
                ('about_ru', models.TextField(null=True, verbose_name='О персонале')),
                ('about_en', models.TextField(null=True, verbose_name='О персонале')),
                ('about_kk', models.TextField(null=True, verbose_name='О персонале')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('educationalPrograms', models.ManyToManyField(blank=True, null=True, to='departments.EducationalPrograms')),
                ('facult', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faculties.facult')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='faculties.page')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.position')),
                ('staffCat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffcat')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонали',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='UserProfileImages/')),
                ('department', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='departments.department')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'admins',
            },
        ),
    ]
