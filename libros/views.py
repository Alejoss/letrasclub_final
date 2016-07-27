# coding=utf-8
import itertools

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from rest_framework import generics

from perfiles.models import City
from libros.models import Libreria, LibroLibreria
from notificaciones.models import Actividad
from libros.serializers import LibroLibreriaSerializer


class Inicio(TemplateView):
    template_name = "libros/inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data()
        context['ciudades_activas'] = City.objects.filter(activa=True, imagen__isnull=False)
        return context


class LibrosCiudad(TemplateView):
    """
    Renderea la vista principal de la ciudad
    """
    template_name = "libros/libros_ciudad.html"

    def get_context_data(self, **kwargs):
        context = super(LibrosCiudad, self).get_context_data()

        ciudad = get_object_or_404(City, id=kwargs['id_ciudad'])
        context['ciudad'] = ciudad

        librerias = Libreria.objects.filter(ciudad=ciudad, eliminada=False)
        libros_destacados = LibroLibreria.objects.filter(eliminado=False, destacado=True,
                                                         libreria__ciudad=ciudad).select_related("libro")
        if not librerias or not libros_destacados:
            pass
            # TODO SI NO HAY LIBRERIAS NI LIBROS DESTACADOS ...

        context['librerias'] = librerias
        context['libros_destacados'] = libros_destacados
        context['actividad'] = Actividad.objects.filter(libro_libreria__libreria__ciudad=ciudad)

        return context


class BuscarLibro(generics.ListAPIView):
    """
    Por ahora búsqueda simple con icontains
    """

    serializer_class = LibroLibreriaSerializer

    def get_queryset(self):
        q = self.kwargs['q']
        ciudad = self.kwargs['id_ciudad']
        libros_por_autor = LibroLibreria.objects.filter(libro__autor__icontains=q, libreria__ciudad=ciudad)
        libros_por_titulo = LibroLibreria.objects.filter(libro__titulo__icontains=q, libreria__ciudad=ciudad)
        resultado_busqueda = itertools.chain(libros_por_titulo, libros_por_autor)

        return resultado_busqueda


class CrearLibro(generics.CreateAPIView):
    """
    Crea un Libro y lo adjudica a un LibroLibrería de un usuario
    """

    serializer_class = LibroLibreriaSerializer
