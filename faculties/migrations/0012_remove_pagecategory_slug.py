# Generated by Django 3.1.6 on 2021-02-11 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0011_pagecategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecategory',
            name='slug',
        ),
    ]