from django.conf.urls import url

from libros import views

urlpatterns = [
    url(r'^ciudad/(?P<slug_ciudad>\w+)/(?P<id_ciudad>\d+)/$', views.LibrosCiudad.as_view(), name="libros_ciudad"),

    # REST API
    url(r'^buscar_libro/(?P<id_ciudad>\d+)/(?P<q>\w+)/$', views.BuscarLibro.as_view(), name="buscar_libro"),
]
