# Generated by Django 3.1.6 on 2021-02-07 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20210207_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 16, 38, 21, 640413), verbose_name='Время'),
        ),
    ]
