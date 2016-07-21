# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from perfiles.models import Perfil
from libros.models import LibroLibreria


class Actividad(models.Model):
    libro_libreria = models.ForeignKey(LibroLibreria)


class Notificacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    perfil = models.ForeignKey(Perfil, null=True, blank=True,
                               related_name="perfil")  # El perfil de la persona que ocasiono la notificación
    segundo_perfil = models.ForeignKey(Perfil, null=True, blank=True,
                                       related_name="segundo_perfil")  # Perfil opcional
    librolibreria = models.ForeignKey(LibroLibreria, null=True, blank=True, related_name="libro")
    segundo_librolibreria = models.ForeignKey(LibroLibreria, null=True, blank=True, related_name="segundo_libro")
    leida = models.BooleanField(default=False)

    # model manager con metodos para crear notificaciones
    objects = NManager()

    class Meta:
        ordering = ["-fecha"]
