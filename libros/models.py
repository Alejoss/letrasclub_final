from __future__ import unicode_literals

from django.db import models

from perfiles.models import Perfil, City


class Libreria(models.Model):
    admin = models.ForeignKey(Perfil)
    ciudad = models.ForeignKey(City)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    ubicacion = models.CharField(max_length=500, blank=True)  # [latitude, longitude]
    direccion = models.CharField(max_length=500, blank=True)
    eliminada = models.BooleanField(default=False)


class Libro(models.Model):
    isbn = models.CharField(blank=True, max_length=50)
    titulo = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    autor = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True, max_length=2500)


class LibroLibreria(models.Model):
    libro = models.ForeignKey(Libro)
    libreria = models.ForeignKey(Libreria)
    destacado = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False)
