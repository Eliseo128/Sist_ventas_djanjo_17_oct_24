from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
]
