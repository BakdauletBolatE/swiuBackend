# Generated by Django 3.1.6 on 2021-04-24 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiupanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widgetitems',
            name='widget',
        ),
        migrations.DeleteModel(
            name='Widget',
        ),
        migrations.DeleteModel(
            name='WidgetItems',
        ),
        migrations.DeleteModel(
            name='WidgetType',
        ),
    ]