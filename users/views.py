from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

from .models import Messages

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            # Autenticamos el usuario
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                # Iniciamos la sesión si el usuario es válido
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



class ChatListView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = "BaseApp/chat.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Messages.objects.order_by('created_at')

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        if content:
            Messages.objects.create(content=content, user=request.user)
        return redirect('Chat')