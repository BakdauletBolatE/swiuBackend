# Generated by Django 3.1.6 on 2021-02-11 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0011_auto_20210211_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageimages',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageImages', to='faculties.page'),
        ),
    ]
