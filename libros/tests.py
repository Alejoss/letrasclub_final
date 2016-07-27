# coding=utf-8
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from perfiles.models import City


class LibrosSitesTest(TestCase):
    def setUp(self):
        self.c = Client()
        # ciudad = City.objects.create(id=)

    def test_inicio(self):
        response = self.c.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

        # Prueba que todas las ciudades sean activas y tengan imagen
        for ciudad in response.context['ciudades_activas']:
            self.assertEqual(ciudad.activa, True)
            self.assertIsNotNone(ciudad.imagen, msg="Ciudad sin imagen en Inicio")

    def test_libros_ciudad(self):
        ciudad = City.objects.get(id=18)
        response = self.c.get(reverse('libros_ciudad', kwargs={'slug_ciudad': ciudad.slug, 'id_ciudad': ciudad.id}))
        self.assertEqual(response.status_code, 200)

        # Prueba que la ciudad esté activa, que haya por lo menos una librería y un libro destacado
        ciudad = response.context['ciudad']
        self.assertEqual(ciudad.activa, True)
        self.assertTrue(len(response.context['librerias']) > 0, msg="No hay librerías en la ciudad")
        self.assertTrue(len(response.context['libros_destacados']) > 0, msg="No hay libros destacados")
