from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from TecnoBlog_App.views import listar_articulos, detallar_articulo, acerca_de_mi, inicio, crear_articulo, eliminar_articulo, editar_articulo


urlpatterns = [
    # URLS de archivos
    path("", inicio, name="inicio"),
    path("articulos/", listar_articulos, name="listar_articulos"),
    path("detalle-articulo/<int:id>/", detallar_articulo, name="detallar_articulo"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
    path("crear-articulo/", crear_articulo, name="crear_articulo"),
    path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
