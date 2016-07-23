from rest_framework import serializers

from perfiles.models import Perfil


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ["usuario", "descripcion", "ciudad", "numero_telefono_contacto"]
