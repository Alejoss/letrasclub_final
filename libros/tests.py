from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class LibrosSitesTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_inicio(self):
        response = self.c.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

        # Prueba que todas las ciudades sean activas y tengan imagen
        for ciudad in response.context['ciudades_activas']:
            self.assertEqual(ciudad.activa, True)
            self.assertIsNotNone(ciudad.imagen, msg="Ciudad sin imagen en Inicio")
