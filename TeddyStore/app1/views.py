from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Usuario
#from .forms import ProductoForm, UsuarioForm

# Función para listar todos los productos (read)
def lista_productos(request):
    productos = Producto.objects.all() # Obtener todos los productos de la base de datos
    return render(request, 'templates/lista_productos.html', {'productos': productos}) #Conectar el html con mis modelos/tablas

# Función para crear un producto
def crear_producto(request):
    if request.method == 'POST': # Verificar si la solicitud es POST (enviar formulario)
        form = ProductoForm(request.POST)  # Inicializar el formulario con los datos enviados
        if form.is_valid(): # Verificar si el formulario es válido
            form.save() # Guardar el  producto ingresado en la base de datos
            return redirect('lista_productos') # Redirigir a la lista de productos
    else:
        form = ProductoForm() # Si la solicitud es GET, mostrar un formulario vacío
    return render(request, 'templates/crear_producto.html', {'form': form}) #Devolvera la pagina crear producto

# Función para actualizar un producto existente
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtener el producto por su id o devolver un 404 si no existe
    if request.method == 'POST': # Verificar si la solicitud es POST (enviar formulario)
        form = ProductoForm(request.POST, instance=producto)  # Inicializar el formulario con los datos enviados y el producto existente
        if form.is_valid(): # Verificar si el formulario es válido
            form.save() # Guardar los cambios en el producto
            return redirect('lista_productos') # Redirigir a la lista de productos
    else:
        form = ProductoForm(instance=producto) # Si la solicitud es GET, mostrar el formulario con los datos del producto existente
    return render(request, 'templates/editar_producto.html', {'form': form}) #Devuelve la pagina completa de editar

# Función para eliminar un usuario existente
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtener el usuario por su id o devolver un 404 si no existe
    if request.method == 'POST':  # Verificar si la solicitud es POST (confirmación de eliminación)
        producto.delete() #Eliminar producto
        return redirect('lista_productos') #Redirigir a la pagina de lista de productos
    return render(request, 'templates/eliminar_producto.html', {'producto': producto}) #Conectar la pagina de eliminar producto con la eliminacionn


###### Vistas para Usuario #########
# Función para listar usuarios (leer)
def lista_usuarios(request):
    usuarios = Usuario.objects.all() #Obtener todos los objetos de el modelo usuarios
    return render(request, 'templates/lista_usuarios.html', {'usuarios': usuarios}) #Conectar usuarios con su template

#Función para crear usuario
def crear_usuario(request):
    if request.method == 'POST': # Verificar si la solicitud es POST (enviar formulario)
        form = UsuarioForm(request.POST) #Inicializar formulario
        if form.is_valid(): #Verificar si el formulario es valido 
            user = form.save() #Guardar usuario registrado
            return redirect('lista_usuarios') #Redirigir al template lista_usuario
    else:
        form = UsuarioForm()  # Si la solicitud es GET, mostrar un formulario vacío
    return render(request, 'templates/crear_usuario.html', {'form': form})  #Conectar formulario con su template

#Función para actualizar usuario
def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id) # Obtener el usuario por su id o devolver un 404 si no existe
    if request.method == 'POST':  # Verificar si la solicitud es POST (formulario enviado)
        form = UsuarioForm(request.POST, instance=usuario)  # Inicializar el formulario con los datos enviados y el usuario existente
        if form.is_valid(): # Verificar si el formulario es válido
            form.save() # Guardar los cambios en los usuarios
            return redirect('lista_usuarios')# Redirigir a la lista de usuarios
    else:
        form = UsuarioForm(instance=usuario) # Si la solicitud es GET, mostrar el formulario con los datos del usuario existente
    return render(request, 'templates/editar_usuario.html', {'form': form})  # Renderizar la página para editar usuario

#Función para eliminar usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id) # Obtener el usuario por su id o devolver un 404 si no existe
    if request.method == 'POST': # Verificar si la solicitud es POST (confirmación de eliminación)
        usuario.user.delete() #Eliminar usuario
        usuario.delete()
        return redirect('lista_usuarios') #Redirigir a la pagina de lista de productos
    return render(request, 'templates/eliminar_usuario.html', {'usuario': usuario}) #Conectar la pagina de eliminar usuario con la eliminacion