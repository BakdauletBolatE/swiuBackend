# Generated by Django 3.1.6 on 2021-03-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0041_auto_20210326_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoryr',
        ),
    ]
