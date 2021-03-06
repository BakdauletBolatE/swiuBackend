# Generated by Django 3.1.5 on 2021-02-01 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0008_auto_20210201_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Должность персонала')),
                ('slug', models.SlugField(verbose_name='Url Должность персонала')),
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
                ('slug', models.SlugField(verbose_name='Url Категория персонала')),
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
                ('name', models.CharField(max_length=255, verbose_name='Имя персонала')),
                ('slug', models.SlugField(verbose_name='Url персонала')),
                ('img', models.ImageField(upload_to='Staff/Posters', verbose_name='Изоброжения персонала')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта персонала')),
                ('adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес персонала')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон персонала')),
                ('about', models.TextField(verbose_name='О персонале')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('educationalPrograms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.educationalprograms')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.position')),
                ('staffCat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffcat')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонали',
            },
        ),
    ]
