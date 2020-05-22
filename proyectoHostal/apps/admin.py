from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ContenidoWeb)
admin.site.register(DatosBanco)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Factura)
admin.site.register(Habitacion)
admin.site.register(HabitacionesReserva)
admin.site.register(Huesped)
admin.site.register(HuespedesReserva)
admin.site.register(Menu)
admin.site.register(OrdenCompra)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(ProductosPedidos)
admin.site.register(ProductosSolicitados)


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','rubro','numero','email')
    list_display_links = ('id','nombre','rubro','numero','email')

pass
admin.site.register(Proveedor,ProveedorAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id','fecha_inicio','fecha_termino','Empresa')
    list_display_links = ('id','fecha_inicio','fecha_termino','Empresa')

    def Empresa(self,obj):
        return obj.fk_id_empresa.nombre

pass
admin.site.register(Reserva,ReservaAdmin)

class RetiroProductoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','hora','Empleado')
    list_display_links = ('id','fecha','hora','Empleado')

    def Empleado(self,obj):
        return obj.fk_id_empleado

pass
admin.site.register(RetiroProducto,RetiroProductoAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio')
    list_display_links = ('id','nombre','descripcion','precio')
pass
admin.site.register(Servicio,ServicioAdmin)


class ServiciosReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicio_nombre','Reserva','Reserva_Fecha_Inicio','Reserva_Fecha_Termino')
    list_display_links= ('id', 'servicio_nombre','Reserva','Reserva_Fecha_Inicio','Reserva_Fecha_Termino')

    def servicio_nombre(self, obj):
        return obj.fk_id_servicio.nombre

    def Reserva(self, obj):
       return obj.fk_id_reserva.id

    def Reserva_Fecha_Inicio(self, obj):
       return obj.fk_id_reserva.fecha_inicio

    def Reserva_Fecha_Termino(self, obj):
       return obj.fk_id_reserva.fecha_termino
    
    pass
admin.site.register(ServiciosReserva,ServiciosReservaAdmin)

class TipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_empleado')
    list_display_links= ('id', 'tipo_empleado')
    pass
admin.site.register(TipoEmpleado,TipoEmpleadoAdmin)
