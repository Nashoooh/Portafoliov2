from django.contrib import admin
from .models import Paciente, Proveedor, Especialista, Reservahora, Empleado, FamiliaProducto, TipoProducto, Producto

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Proveedor)
admin.site.register(Especialista)
admin.site.register(Reservahora)
admin.site.register(Empleado)
admin.site.register(FamiliaProducto)
admin.site.register(TipoProducto)
admin.site.register(Producto)
