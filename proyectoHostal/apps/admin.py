from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

class ContenidoWebForm(forms.ModelForm):
    contenido = forms.CharField( widget=forms.Textarea )
    class meta:
        model = ContenidoWeb

class ContenidoWebAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','servicio')
    list_display_links = ('id','nombre','servicio')
    form = ContenidoWebForm
    def servicio(self,obj):
        return obj.fk_id_servicio

pass
admin.site.register(ContenidoWeb,ContenidoWebAdmin)

class DatosBancoAdmin(admin.ModelAdmin):
    list_display = ('numero_cuenta','banco','tipo_cuenta')
    list_display_links = ('numero_cuenta','banco','tipo_cuenta')
    
pass
admin.site.register(DatosBanco,DatosBancoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','email','numero','Cargo','nro_cuenta')
    list_display_links = ('rut','nombre','email','numero','Cargo','nro_cuenta')
    
    def Cargo(self,obj):
        return obj.fk_id_tipo_empleado
    def nro_cuenta(self,obj):
        return obj.fk_numero_cuenta

pass
admin.site.register(Empleado,EmpleadoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','rut','nombre','email','numero')
    list_display_links = ('id','rut','nombre','email','numero')
    
pass
admin.site.register(Empresa,EmpresaAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id','rut_empresa','orden_de_compra')
    list_display_links = ('id','rut_empresa','orden_de_compra')
    
    def orden_de_compra(self,obj):
        return obj.fk_id_orden_compra

pass
admin.site.register(Factura,FacturaAdmin)

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id','numero_habitacion','tipo_cama','precio','estado')
    list_display_links = ('id','numero_habitacion','tipo_cama','precio','estado')
        
pass
admin.site.register(Habitacion,HabitacionAdmin)

class HabitacionesReservaAdmin(admin.ModelAdmin):
    list_display = ('id','reserva','huesped')
    list_display_links = ('id','reserva','huesped')

    def huesped(self,obj):
        return obj.fk_id_huesped
    def reserva(self,obj):
        return obj.fk_id_reserva
        
pass
admin.site.register(HabitacionesReserva,HabitacionesReservaAdmin)

class HuespedAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','rut','empresa')
    list_display_links = ('id','nombre','rut','empresa')

    def empresa(self,obj):
        return obj.fk_id_empresa

pass
admin.site.register(Huesped,HuespedAdmin)

class HuespedesReservaAdmin(admin.ModelAdmin):
    list_display = ('id','reserva','huesped')
    list_display_links = ('id','reserva','huesped')

    def reserva(self,obj):
        return obj.fk_id_reserva
    def huesped(self,obj):
        return obj.fk_id_huesped
pass
admin.site.register(HuespedesReserva,HuespedesReservaAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_menu','precio')
    list_display_links = ('id','tipo_menu','precio')

pass
admin.site.register(Menu,MenuAdmin)

class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('id','monto_pago','reserva')
    list_display_links = ('id','monto_pago','reserva')

    def reserva(self,obj):
        return obj.fk_id_reserva

pass
admin.site.register(OrdenCompra,OrdenCompraAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','monto_total','estado','proveedor')
    list_display_links = ('id','monto_total','estado','proveedor')

    def proveedor(self,obj):
        return obj.fk_id_proveedor

pass
admin.site.register(Pedido,PedidoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','stock','nombre','tipo_producto','marca','proveedor')
    list_display_links = ('id','stock','nombre','tipo_producto','marca','proveedor')

    def proveedor(self,obj):
        return obj.fk_id_proveedor

pass
admin.site.register(Producto,ProductoAdmin)

class ProductosPedidosAdmin(admin.ModelAdmin):
    list_display = ('id','cantidad','producto','id_pedido')
    list_display_links = ('id','cantidad','producto','id_pedido')

    def producto(self,obj):
        return obj.fk_id_producto.nombre
    def id_pedido(self,obj):
        return obj.fk_id_pedido.id

pass
admin.site.register(ProductosPedidos,ProductosPedidosAdmin)

class ProductosSolicitadosAdmin(admin.ModelAdmin):
    list_display = ('id','cantidad','producto','id_retiro')
    list_display_links = ('id','cantidad','producto','id_retiro')

    def producto(self,obj):
        return obj.fk_id_producto.nombre
    def id_retiro(self,obj):
        return obj.fk_retiro_producto.id

pass
admin.site.register(ProductosSolicitados,ProductosSolicitadosAdmin)

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
