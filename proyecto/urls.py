from django.contrib import admin
from django.urls import path
from facturacion.index import index
from facturacion.cliente import *
from facturacion.producto import *
from facturacion.factura import *

urlpatterns = [
    path('', index, name='Index'),
    path('ventas/', listarVenta, name='ventas'),
    path('clientes/', listarCliente, name='clientes'),
    path('agregarCliente/', agregarCliente, name='agregarCliente'),
    path('editarCliente/<int:id>/', editarCliente, name='editarCliente'),
    path('eliminarCliente/<int:id>/', eliminarCliente, name='eliminarCliente'),
    path('productos/', listarProducto, name='productos'),
    path('agregarProducto/', agregarProducto, name='agregarProducto'),
    path('editarProducto/<int:id>/', editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),
    path('admin/', admin.site.urls),
]
