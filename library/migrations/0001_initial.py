# Generated by Django 3.1.6 on 2021-02-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0011_auto_20210202_1131'),
        ('staff', '0002_auto_20210202_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, verbose_name='Год')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('img', models.ImageField(upload_to='Book/Posters/')),
                ('pdffile', models.FileField(upload_to='Book/Pdf')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('eduProgram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.educationalprograms')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.year')),
            ],
        ),
    ]
