# Generated by Django 3.1.6 on 2021-02-11 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20210211_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 13, 50, 15, 63202), verbose_name='Время'),
        ),
    ]