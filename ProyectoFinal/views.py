# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import handler404

# Create your views here.
def inicio(req):
  return HttpResponse("<h1>Proyecto Python Pedro Sanchez</h1><a href=\"BaseApp\"><button>Ir a la App</button></a></br></br><a href=\"admin\"><button>Admin Panel</button></a>")
