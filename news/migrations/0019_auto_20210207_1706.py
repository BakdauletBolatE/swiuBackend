# Generated by Django 3.1.6 on 2021-02-07 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20210207_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 17, 6, 42, 358906), verbose_name='Время'),
        ),
    ]
