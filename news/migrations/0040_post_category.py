# Generated by Django 3.1.6 on 2021-03-26 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20210326_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.postcategories'),
            preserve_default=False,
        ),
    ]
