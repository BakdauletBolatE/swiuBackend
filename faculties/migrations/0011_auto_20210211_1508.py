# Generated by Django 3.1.6 on 2021-02-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0010_auto_20210211_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
    ]
