from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from Perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from Perfiles.models import Avatar

# Create your views here.
# Funcion REGISTRAR USUARIO:
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
    
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name= 'Perfiles/registro.html',
        context={ 'form': formulario},
    )


# Funcion INICAR SESION USUARIO
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password) #user puede ser un usuario o None
            
            if user:
                login(request=request, user=user)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    
    return render(
        request=request,
        template_name='Perfiles/login.html',
        context={'form': form},
    )

# Funcion CERRAR SESION USUARIO:
class CustomLogoutView(LogoutView):
    template_name = 'Perfiles/logout.html'

# Funcion EDITAR USUARIO:
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'Perfiles/formulario_perfil.html'

    def get_object(self, QuerySet=None):
        return self.request.user
    
# Funcion AGREGAR AVATAR:
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario()

    return render(
        request=request,
        template_name="Perfiles/formulario_avatar.html",
        context={'form': formulario},
    )
# EDITAR AVATAR
def editar_avatar(request):
    avatar = Avatar.objects.get(user=request.user)  # Obtén el avatar del usuario actual

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario(instance=avatar)

    return render(
        request=request,
        template_name="Perfiles/formulario_avatar.html",
        context={'form': formulario},
    )