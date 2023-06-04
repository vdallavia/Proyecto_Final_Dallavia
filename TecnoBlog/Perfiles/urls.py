from django.contrib import admin
from django.urls import URLPattern, path
from django.conf.urls.static import static
from django.conf import settings

from Perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar
urlspatterns = [
    path('admin/', admin.site.urls),
    path("registro/", registro, name="registro"),
    path("login/", login_view, name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("editar-mi-perfil/", MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path("agregar-avatar/", agregar_avatar, name="agregar_avatar"),
]

urlspatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)