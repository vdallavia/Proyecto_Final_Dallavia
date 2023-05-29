from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Perfiles.models import Avatar

# Definición clase Registrar Usuario:
class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

# Definición clase Registrar Usuario:
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name','email']

# Definición clase Avatar:
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']