# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0002_auto_20160722_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libreria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=500)),
                ('direccion', models.CharField(blank=True, max_length=500)),
                ('eliminada', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.Perfil')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfiles.City')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, max_length=50)),
                ('titulo', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('autor', models.CharField(blank=True, max_length=255)),
                ('descripcion', models.TextField(blank=True, max_length=2500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibroLibreria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destacado', models.BooleanField(default=False)),
                ('eliminado', models.BooleanField(default=False)),
                ('libreria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Libreria')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Libro')),
            ],
        ),
    ]
