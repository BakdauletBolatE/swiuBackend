# Generated by Django 3.1.6 on 2021-02-11 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0006_auto_20210211_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='НАзвани катоегрий')),
            ],
            options={
                'verbose_name': 'НАзвани катоегрий',
                'verbose_name_plural': 'НАзвани катоегрий',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='page', to='faculties.pagecategory'),
            preserve_default=False,
        ),
    ]
