# Generated by Django 3.1.6 on 2021-02-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0003_auto_20210202_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='facult',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание факультета'),
        ),
        migrations.AddField(
            model_name='facult',
            name='description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание факультета'),
        ),
        migrations.AddField(
            model_name='facult',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание факультета'),
        ),
        migrations.AddField(
            model_name='facult',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название факультета'),
        ),
        migrations.AddField(
            model_name='facult',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название факультета'),
        ),
        migrations.AddField(
            model_name='facult',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название факультета'),
        ),
    ]