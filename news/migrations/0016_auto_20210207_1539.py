# Generated by Django 3.1.6 on 2021-02-07 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20210206_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 15, 39, 44, 733288), verbose_name='Время'),
        ),
    ]
