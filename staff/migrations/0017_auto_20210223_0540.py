# Generated by Django 3.1.6 on 2021-02-23 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0012_auto_20210211_1108'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0016_auto_20210223_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='departments.department'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
