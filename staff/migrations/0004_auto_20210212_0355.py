# Generated by Django 3.1.6 on 2021-02-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0012_auto_20210211_1108'),
        ('staff', '0003_auto_20210211_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='educationalPrograms',
        ),
        migrations.AddField(
            model_name='staff',
            name='educationalPrograms',
            field=models.ManyToManyField(blank=True, null=True, to='departments.EducationalPrograms'),
        ),
    ]