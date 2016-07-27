from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

from perfiles.models import Perfil, City


class Libreria(models.Model):
    admin = models.ForeignKey(Perfil)
    nombre = models.CharField(max_length=255, blank=True, unique=True)
    ciudad = models.ForeignKey(City)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    ubicacion = models.CharField(max_length=500, blank=True)  # [latitude, longitude]
    direccion = models.CharField(max_length=500, blank=True)
    eliminada = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)

        super(Libreria, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug


class Libro(models.Model):
    isbn = models.CharField(blank=True, max_length=50)
    titulo = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    autor = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True, max_length=2500)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)

        super(Libro, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo


class LibroLibreria(models.Model):
    libro = models.ForeignKey(Libro)
    libreria = models.ForeignKey(Libreria)
    destacado = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.libro, self.libreria)
