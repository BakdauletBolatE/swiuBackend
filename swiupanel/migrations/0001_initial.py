# Generated by Django 3.1.6 on 2021-03-26 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название виджета')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widgets', to='faculties.page', verbose_name='Страница которому нужно подключиться')),
            ],
        ),
        migrations.CreateModel(
            name='WidgetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название типа виджета?')),
            ],
        ),
        migrations.CreateModel(
            name='WidgetItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Загаловок виджета')),
                ('widget_photo', models.ImageField(blank=True, null=True, upload_to='WidgetImages/', verbose_name='Фото для виджета')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контентная часть виджета')),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widgetitems', to='swiupanel.widget', verbose_name='Виджет')),
            ],
        ),
        migrations.AddField(
            model_name='widget',
            name='widget_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='widget', to='swiupanel.widgettype', verbose_name='Тип виджета которому нужно подключиться'),
        ),
    ]
