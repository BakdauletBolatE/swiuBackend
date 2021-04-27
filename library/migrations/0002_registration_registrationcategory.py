# Generated by Django 3.1.6 on 2021-04-26 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20210422_1327'),
        ('library', '0001_initial'),
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
    ]