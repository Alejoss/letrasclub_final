from rest_framework import serializers

from libros.models import LibroLibreria, Libro, Libreria
from perfiles.models import City, Perfil


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ["isbn", "titulo", "autor", "descripcion"]


class LibreriaSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all())
    ciudad = serializers.SlugRelatedField(slug_field='name', queryset=City.objects.all())

    class Meta:
        model = Libreria
        fields = ["ubicacion", "direccion", "eliminada", "admin", "ciudad"]


class LibroLibreriaSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()
    libreria = serializers.SlugRelatedField(slug_field="nombre", queryset=Libreria.objects.all())

    def create(self, validated_data):
        print validated_data
        libreria_slug = validated_data['libreria']
        libreria = Libreria.objects.get(slug=libreria_slug)
        libro = Libro.objects.create(
            isbn=validated_data['libro']['isbn'],
            titulo=validated_data['libro']['titulo'],
            autor=validated_data['libro']['autor'],
            descripcion=validated_data['libro']['descripcion'],
        )
        libro_libreria = LibroLibreria.objects.create(libro=libro, libreria=libreria)
        return libro_libreria

    class Meta:
        model = LibroLibreria
        fields = ["destacado", "eliminado", "libro", "libreria", "id"]
