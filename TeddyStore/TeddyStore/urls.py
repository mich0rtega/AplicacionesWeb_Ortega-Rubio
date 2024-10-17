"""
URL configuration for TeddyStore project.

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
from django.contrib import admin
from django.urls import path
from app1.views import (
    UsuariosListView, UsuariosCreateView, UsuariosUpdateView, UsuariosDeleteView,
    ProductosListView, ProductosCreateView, ProductosUpdateView, ProductosDeleteView
)

urlpatterns = [
    # CRUD Usuarios
    path('usuarios/', UsuariosListView.as_view(), name='usuarios-list'),
    path('usuarios/new/', UsuariosCreateView.as_view(), name='usuarios-create'),
    path('usuarios/<int:pk>/edit/', UsuariosUpdateView.as_view(), name='usuarios-update'),
    path('usuarios/<int:pk>/delete/', UsuariosDeleteView.as_view(), name='usuarios-delete'),

    # CRUD Productos
    path('productos/', ProductosListView.as_view(), name='productos-list'),
    path('productos/new/', ProductosCreateView.as_view(), name='productos-create'),
    path('productos/<int:pk>/edit/', ProductosUpdateView.as_view(), name='productos-update'),
    path('productos/<int:pk>/delete/', ProductosDeleteView.as_view(), name='productos-delete'),
]
