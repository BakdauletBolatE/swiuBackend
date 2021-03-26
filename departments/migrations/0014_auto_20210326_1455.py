# Generated by Django 3.1.6 on 2021-03-26 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0022_page_order'),
        ('departments', '0013_auto_20210316_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydepartment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.activitydepartmentcat'),
        ),
        migrations.AlterField(
            model_name='activitydepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
        migrations.AlterField(
            model_name='educationalprograms',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.educationalprogramscat'),
        ),
        migrations.AlterField(
            model_name='educationalprograms',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
        ),
        migrations.AlterField(
            model_name='educationalprograms',
            name='facult',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.facult'),
        ),
    ]