from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .models import Messages, Imagen

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "BaseApp/index.html")
            else:
                msg_login = "Usuario o contraseña incorrectos"
        else:
            msg_login = "Formulario no válido"

    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"BaseApp/index.html")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


@login_required 
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()

            miFormulario.save()

            return render(request, "BaseApp/index.html")

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "users/edit-profile.html", {"mi_form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/edit-pass.html"
    success_url = reverse_lazy("Profile")



class ChatListView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = "users/chat.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Messages.objects.order_by('created_at')

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        if content:
            Messages.objects.create(content=content, user=request.user)
        return redirect('Chat')