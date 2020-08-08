from django.contrib import admin
from django.contrib import admin
from django.forms import Textarea
from django.contrib.admin import AdminSite
from facturacion.models import *


class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    extra = 1
    can_delete = True
    show_change_link = True


class FacturaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 60})
        },
    }

    inlines = (DetalleFacturaInline,)
    list_display = (
        'fecha',
        'cliente',
        'total',
    )

    ordering = ('-fecha',)
    search_fields = ('cliente', 'fecha')
    list_filter = (
        'cliente__nombre',
        'fecha',
    )


admin.site.register(Factura, FacturaAdmin)
