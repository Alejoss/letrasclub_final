from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


from perfiles.models import City
from libros.models import Libreria, LibroLibreria
from notificaciones.models import Actividad


class Inicio(TemplateView):
    template_name = "libros/inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data()
        context['ciudades_activas'] = City.objects.filter(activa=True)
        return context


def libros_ciudad(request, slug_ciudad, id_ciudad):
    """
    Renderea la vista principal de la ciudad
    """
    template = "libros/libros_ciudad.html"

    ciudad = get_object_or_404(City, id=id_ciudad)
    librerias = Libreria.objects.filter(ciudad=ciudad, eliminada=False)

    libros_destacados = LibroLibreria.objects.filter(eliminado=False, destacado=True, libreria__ciudad=ciudad).select_related("libro")

    actividad = Actividad.objects.filter(libro_libreria__libreria__ciudad=ciudad)

    context = {}

    return render(request, template, context)
