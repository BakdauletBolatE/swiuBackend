# Generated by Django 3.1.6 on 2021-03-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_auto_20210223_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Филтрация'),
        ),
    ]
