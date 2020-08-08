from django.shortcuts import render, redirect
from facturacion.models import Factura


def listarVenta(request):
    lista = Factura.objects.all().order_by('pk')
    opciones = {'menu': 'Mantenimiento Factura',
                'modulo': 'Factura',
                'listado': lista}
    return render(request, 'listar_factura.html', opciones)
