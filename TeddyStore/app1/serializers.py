
from rest_framework import serializers
from .models import Usuarios, Productos

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['usuario', 'password', 'direccion', 'telefono']

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['cod_producto', 'nombre', 'descripcion', 'precio', 'stock']
