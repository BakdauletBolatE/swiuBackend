# Generated by Django 3.1.6 on 2021-02-15 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0018_auto_20210213_0816'),
        ('staff', '0012_auto_20210214_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='faculties.page'),
        ),
    ]
