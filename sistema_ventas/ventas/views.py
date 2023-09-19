from django.shortcuts import render

# Create your views here.
from .models import Proveedor, Cliente, Producto, Venta

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/lista_proveedores.html', {'proveedores': proveedores})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})
