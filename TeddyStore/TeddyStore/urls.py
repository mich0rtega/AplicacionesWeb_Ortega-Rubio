from django.urls import path
from django.contrib import admin  # Importa admin desde django.contrib
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('producto/<int:cod_producto>/', views.vista_producto, name='vista_producto'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:cod_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('actualizar_producto/<int:cod_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('login/', views.login_view, name='login'),
]
