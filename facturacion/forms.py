from django import forms
from facturacion.models import Cliente, Producto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'direccion', 'producto')
        label = {'nombre': 'Nombres Completos', 'ruc': 'Ruc', 'direccion': 'Dirección', 'producto': 'Productos'}
        widgets = {

            'nombre': forms.TextInput(attrs={'class': "form-control",
                                              "placeholder": "Ingrese Nombre"}),

            'ruc':  forms.TextInput(
                attrs={'class': "form-control", 'required': 'True',
                       "placeholder": "Ingrese Ruc"}),

            'direccion':  forms.TextInput(
                attrs={'class': "form-control", 'required': 'True',
                       "placeholder": "Ingrese Dirección"}),

            'producto': forms.SelectMultiple(attrs={'class': "form-control "}),

        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripción', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}
        widgets = {

            'descripcion': forms.TextInput(attrs={'class': "form-control",
                                              "placeholder": "Ingrese Descripción"}),

            'precio':  forms.TextInput(
                attrs={'class': "form-control", 'required': 'True', 'type': 'number',
                       "placeholder": "Ingrese Precio"}),

            'stock':  forms.TextInput(
                attrs={'class': "form-control", 'required': 'True', 'type': 'number',
                       "placeholder": "Ingrese Stock"}),

            'iva': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),

        }

