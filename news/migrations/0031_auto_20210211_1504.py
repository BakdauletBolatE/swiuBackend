# Generated by Django 3.1.6 on 2021-02-11 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20210211_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 15, 4, 0, 418315), verbose_name='Время'),
        ),
    ]
