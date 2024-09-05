from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Guitar, Bass, Client



# Vistas públicas
def inicio(req):
  return render(req, 'BaseApp/index.html')

def about(req):
  return render(req, 'BaseApp/about.html')



# Todas las vistas del modelo Guitar
class GuitarListView(LoginRequiredMixin, ListView):
  model = Guitar
  template_name = "BaseApp/guitarras.html"

  def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)
    
class GuitarDetailView(LoginRequiredMixin, DetailView):
  model = Guitar
  template_name = "BaseApp/guitar-detail.html"

class GuitarCreateView(LoginRequiredMixin, CreateView):
  model = Guitar
  template_name = "BaseApp/guitar-form.html"
  fields = ["name", "brand", "model", "color", "price", "description"]

  success_url = reverse_lazy("Guitarras")

class GuitarUpdateView(LoginRequiredMixin, UpdateView):
    model = Guitar
    success_url = reverse_lazy("Guitarras")
    fields = ["name", "brand", "model", "color", "price", "description"]
    template_name = "BaseApp/guitar-update.html"

class GuitarDeleteView(LoginRequiredMixin, DeleteView):
    model = Guitar
    success_url = reverse_lazy("Guitarras")
    template_name = 'BaseApp/guitar-delete.html'



# Todas las vistas del modelo Bass
class BassListView(LoginRequiredMixin, ListView):
  model = Bass
  template_name = "BaseApp/bajos.html"

  def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)
    
class BassDetailView(LoginRequiredMixin, DetailView):
  model = Bass
  template_name = "BaseApp/bass-detail.html"

class BassCreateView(LoginRequiredMixin, CreateView):
  model = Bass
  template_name = "BaseApp/bass-form.html"
  fields = ["name", "brand", "model", "color", "price", "description"]

  success_url = reverse_lazy("Bajos")

class BassUpdateView(LoginRequiredMixin, UpdateView):
    model = Bass
    success_url = reverse_lazy("Bajos")
    fields = ["name", "brand", "model", "color", "price", "description"]
    template_name = "BaseApp/bass-update.html"

class BassDeleteView(LoginRequiredMixin, DeleteView):
    model = Bass
    success_url = reverse_lazy("Bajos")
    template_name = 'BaseApp/bass-delete.html'


# Todas las vistas del modelo Client
class ClientListView(LoginRequiredMixin, ListView):
  model = Client
  template_name = "BaseApp/clientes.html"

  def get(self, request, *args, **kwargs):
    return super().get(request, *args, **kwargs)
    
class ClientDetailView(LoginRequiredMixin, DetailView):
  model = Client
  template_name = "BaseApp/client-detail.html"

class ClientCreateView(LoginRequiredMixin, CreateView):
  model = Client
  template_name = "BaseApp/client-form.html"
  fields = ["name", "surname", "email"]

  success_url = reverse_lazy("Clientes")

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy("Clientes")
    fields = ["name", "surname", "email"]
    template_name = "BaseApp/client-update.html"

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("Clientes")
    template_name = 'BaseApp/client-delete.html'



# Búsqueda por nombre en los modelos
@login_required
def guitarSearch(req):
  return render(req, 'BaseApp/search-guitar.html')

@login_required
def bassSearch(req):
  return render(req, 'BaseApp/search-bass.html')

@login_required
def clientSearch(req):
  return render(req, 'BaseApp/search-client.html')


# Resultados de la búsqueda
@login_required
def searchResults(req):
  guitar_query = req.GET.get('guitar')
  bass_query = req.GET.get('bass')
  client_query = req.GET.get('client')
  
  if guitar_query:
    nombre = guitar_query
    guitarras = Guitar.objects.filter(name__icontains=nombre)
    print(guitarras)
    return render(req, "BaseApp/results.html", { "name": nombre, "guitars": guitarras })

  elif bass_query:
    nombre = bass_query
    bajos = Bass.objects.filter(name__icontains=nombre)
    return render(req, "BaseApp/results.html", { "name": nombre, "basses": bajos })

  elif client_query:
    nombre = client_query
    clientes = Client.objects.filter(name__icontains=nombre)
    return render(req, "BaseApp/results.html", { "name": nombre, "clients": clientes })

  else:
    respuesta = "No enviaste nada"

  return HttpResponse(respuesta)


# Página 404 custom
# Esto solo funciona si `DEGUB = False` en settings.py
def handling_404(req, exception):
  return render(req, '404.html', {})