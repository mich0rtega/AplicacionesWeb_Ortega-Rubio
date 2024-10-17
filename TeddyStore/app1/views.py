from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuarios, Productos
# Create your views here.

############### Usuarios #############
#Ver Usuario
class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'templates/usuarios-list.html'
    context_object_name = 'usuarios'

#Crear Usuario
class UsuariosCreateView(CreateView):
    model = Usuarios
    template_name = 'templates/usuarios_crear.html'
    fields = ['usuario', 'password', 'direccion', 'telefono']
    success_url = reverse_lazy('usuarios-list')

#Actualizar Usuario
class UsuariosUpdateView(UpdateView):
    model = Usuarios
    template_name = 'usuarios/usuarios_actualizar.html'
    fields = ['password', 'direccion', 'telefono']
    success_url = reverse_lazy('usuarios-list')

#Eliminar Usuario
class UsuariosDeleteView(DeleteView):
    model = Usuarios
    template_name = 'usuarios/usuarios_eliminar.html'
    success_url = reverse_lazy('usuarios-list')

################ Productos ###############
#Ver producto
class ProductosListView(ListView):
    model = Productos
    template_name = 'productos/productos_list.html'
    context_object_name = 'productos'

#Insertar producto
class ProductosCreateView(CreateView):
    model = Productos
    template_name = 'productos/productos_crear.html'
    fields = ['cod_producto', 'nombre', 'descripcion', 'precio', 'stock']
    success_url = reverse_lazy('productos-list')

#Actualizar producto
class ProductosUpdateView(UpdateView):
    model = Productos
    template_name = 'productos/productos_actualizar.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    success_url = reverse_lazy('productos-list')

#Eliminar productos
class ProductosDeleteView(DeleteView):
    model = Productos
    template_name = 'productos/productos_eliminar.html'
    success_url = reverse_lazy('productos-list')



