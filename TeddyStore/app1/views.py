
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios, Productos
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'mi_app/index.html', {'productos': Productos.objects.all()})

def vista_producto(request, cod_producto):
    producto = get_object_or_404(Productos, cod_producto=cod_producto)
    return render(request, 'mi_app/vista_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        # Lógica para agregar un producto
        # ...
        return redirect('index')
    return render(request, 'mi_app/agregar_producto.html')

def eliminar_producto(request, cod_producto):
    producto = get_object_or_404(Productos, cod_producto=cod_producto)
    producto.delete()
    return redirect('index')

def actualizar_producto(request, cod_producto):
    producto = get_object_or_404(Productos, cod_producto=cod_producto)
    if request.method == 'POST':
        # Lógica para actualizar el producto
        # ...
        return redirect('index')
    return render(request, 'mi_app/actualizar_producto.html', {'producto': producto})

def lista_usuarios(request):
    return render(request, 'mi_app/lista_usuarios.html', {'usuarios': Usuarios.objects.all()})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'mi_app/login.html')
