# Generated by Django 3.1.6 on 2021-02-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0012_auto_20210211_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий'),
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий'),
        ),
        migrations.AddField(
            model_name='pagecategory',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='НАзвани катоегрий'),
        ),
    ]
