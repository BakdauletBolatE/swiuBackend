# Generated by Django 3.1.6 on 2021-04-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20210425_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetonlytext',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetonlytext',
            name='description_kk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetonlytext',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='description_kk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='title_kk',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='widgetphoto',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='description_kk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='title_kk',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='widgettext',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
