# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libreria',
            name='nombre',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]