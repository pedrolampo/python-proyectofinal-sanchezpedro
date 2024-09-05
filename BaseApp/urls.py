from django.urls import path
from . import views

urlpatterns = [
  path('', views.inicio, name='Inicio'),
  path('about/', views.about, name='About'),
  
  # Guitarras
  path('guitarras/', views.GuitarListView.as_view(), name='Guitarras'),
  path('guitarras/<int:pk>/', views.GuitarDetailView.as_view(), name="GuitarDetail"),
  path('guitarras/create/', views.GuitarCreateView.as_view(), name='GuitarCreate'),
  path('guitarras/update/<int:pk>/', views.GuitarUpdateView.as_view(), name='GuitarUpdate'),
  path('guitarras/delete/<int:pk>/', views.GuitarDeleteView.as_view(), name='GuitarDelete'),
  path('guitarras/search/', views.guitarSearch, name='GuitarSearch'),

  # Bajos
  path('bajos/', views.BassListView.as_view(), name='Bajos'),
  path('bajos/<int:pk>/', views.BassDetailView.as_view(), name="BassDetail"),
  path('bajos/create/', views.BassCreateView.as_view(), name='BassCreate'),
  path('bajos/update/<int:pk>/', views.BassUpdateView.as_view(), name='BassUpdate'),
  path('bajos/delete/<int:pk>/', views.BassDeleteView.as_view(), name='BassDelete'),
  path('bajos/search/', views.bassSearch, name='BassSearch'),

  # Clientes
  path('clientes/', views.ClientListView.as_view(), name='Clientes'),
  path('clientes/<int:pk>/', views.ClientDetailView.as_view(), name="ClientDetail"),
  path('clientes/create/', views.ClientCreateView.as_view(), name='ClientCreate'),
  path('clientes/update/<int:pk>/', views.ClientUpdateView.as_view(), name='ClientUpdate'),
  path('clientes/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='ClientDelete'),
  path('clientes/search/', views.clientSearch, name='ClientSearch'),

  path('search-results/', views.searchResults, name='SearchResults'),
]
