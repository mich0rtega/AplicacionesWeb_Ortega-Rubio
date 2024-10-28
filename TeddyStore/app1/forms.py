from django import forms
from .models import Producto, Usuario  # Asegúrate de tener los modelos de Producto y Usuario definidos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción del producto'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Precio'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Cantidad en stock'}),
            'imagen': forms.ClearableFileInput(attrs={'placeholder': 'URL de la imagen'}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre Completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Número de Teléfono'}),
        }
