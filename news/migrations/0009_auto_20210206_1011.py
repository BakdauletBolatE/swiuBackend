# Generated by Django 3.1.6 on 2021-02-06 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_postcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='post_img', to='news.post'),
        ),
    ]