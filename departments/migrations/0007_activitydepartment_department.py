# Generated by Django 3.1.5 on 2021-02-01 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0006_auto_20210201_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydepartment',
            name='department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
    ]
