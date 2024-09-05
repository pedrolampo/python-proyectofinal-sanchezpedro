from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserEditForm(UserChangeForm):
    password = None

    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    description = forms.CharField(label='Descripción', required=False)
    website = forms.CharField(label='Página Web', required=False)

    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['email',
                'last_name',
                'first_name',
                'imagen',
                'description',
                'website'
            ]  


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]