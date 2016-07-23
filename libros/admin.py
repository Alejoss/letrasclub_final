from django.contrib import admin

from libros.models import Libro, LibroLibreria, Libreria

admin.site.register(Libro)
admin.site.register(LibroLibreria)
admin.site.register(Libreria)
