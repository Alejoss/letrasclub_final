from django.conf.urls import url

from libros import views

urlpatterns = [
    url(r'^ciudad/(?P<slug_ciudad>\w+)/(?P<id_ciudad>\d+)/$', views.LibrosCiudad.as_view(), name="libros_ciudad"),

    # REST API
    url(r'^buscar_libro/(?P<id_ciudad>\d+)/(?P<q>\w+)/$', views.BuscarLibro.as_view(), name="buscar_libro"),
    url(r'^crear_libro/$', views.CrearLibro.as_view(), name="crear_libro"),
    url(r'^editar_libro/(?P<id_libro>\d+)/$', views.EditarLibro.as_view(), name="editar_libro"),
]
