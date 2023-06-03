"""
URL configuration for TecnoBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from TecnoBlog_App.views import listar_articulos, detallar_articulo, acerca_de_mi, inicio, crear_articulo, eliminar_articulo, editar_articulo
from Perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar

urlpatterns = [
     path('admin/', admin.site.urls),
     path("", inicio, name="inicio"),
     path("articulos/", listar_articulos, name="listar_articulos"),
     path("detalle-articulo/", detallar_articulo, name="detallar_articulo"),
     path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
     path("crear-articulo/", crear_articulo, name="crear_articulo"),
     path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
     path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
     path("registro/", registro, name="registro"),
     path("login/", login_view, name="login"),
     path("logout/", CustomLogoutView.as_view(), name="logout"),
     path("editar-mi-perfil/", MiPerfilUpdateView.as_view(), name="editar_perfil"),
     path("agregar-avatar/", agregar_avatar, name="agregar_avatar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)