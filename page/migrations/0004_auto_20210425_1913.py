# Generated by Django 3.1.6 on 2021-04-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_widget_iic_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='iic_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]