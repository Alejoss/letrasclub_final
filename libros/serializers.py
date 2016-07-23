from rest_framework import serializers

from libros.models import LibroLibreria, Libro, Libreria


class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ["isbn", "titulo", "slug", "autor", "descripcion"]


class LibreriaSerializer(serializers.ModelSerializer):

    admin = serializers.PrimaryKeyRelatedField(read_only=True)
    ciudad = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Libreria
        fields = ["slug", "ubicacion", "direccion", "eliminada", "admin", "ciudad"]


class LibroLibreriaSerializer(serializers.ModelSerializer):

    libro = LibroSerializer(read_only=True)

    class Meta:
        model = LibroLibreria
        fields = ["destacado", "eliminado", "libro"]
