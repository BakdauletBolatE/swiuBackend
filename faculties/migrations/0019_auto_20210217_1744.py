# Generated by Django 3.1.6 on 2021-02-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0018_auto_20210213_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Page/', verbose_name='Постер страницы'),
        ),
    ]
