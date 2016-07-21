from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from cities_light.abstract_models import AbstractCity, AbstractRegion, AbstractCountry
from cities_light.receivers import connect_default_signals


class Country(AbstractCountry):
    pass
connect_default_signals(Country)


class Region(AbstractRegion):
    pass
connect_default_signals(Region)


class City(AbstractCity):
    activa = models.BooleanField(default=False)
    imagen = models.ImageField(null=True)
    fecha_activacion = models.DateTimeField(null=True)
connect_default_signals(City)


class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    imagen_perfil = models.URLField(blank=True)
    descripcion = models.CharField(max_length=250, blank=True)

    ciudad = models.ForeignKey(City, null=True, blank=True)
    numero_telefono_contacto = models.CharField(blank=True, max_length=55)

    @property
    def datos_contacto(self):

        if not self.numero_telefono_contacto and not self.usuario.email:
            return False
        else:
            datos_contacto = {'telefono': self.numero_telefono_contacto, 'email': self.usuario.email}
            return datos_contacto

    def __unicode__(self):
        return "Perfil: %s" % self.usuario.username
