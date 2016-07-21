from django.conf.urls import url

from libros import views

urlpatterns = [
    url(r'^ciudad/(?P<slug_ciudad>\w+)/(?P<id_ciudad>\d+)/$', views.libros_ciudad, name="libros_ciudad")
]
