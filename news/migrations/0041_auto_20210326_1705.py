# Generated by Django 3.1.6 on 2021-03-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0040_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoryr',
        ),
    ]
