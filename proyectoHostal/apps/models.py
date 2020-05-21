# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContenidoWeb(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    contenido = models.CharField(max_length=100, blank=True, null=True)
    fk_id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='fk_id_servicio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contenido_web'


class DatosBanco(models.Model):
    numero_cuenta = models.BigIntegerField(primary_key=True)
    banco = models.CharField(max_length=20, blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_banco'


class Empleado(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    fk_id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='fk_id_tipo_empleado', blank=True, null=True)
    fk_numero_cuenta = models.ForeignKey(DatosBanco, models.DO_NOTHING, db_column='fk_numero_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    numero = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'empresa'


class Factura(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rut_empresa = models.CharField(max_length=10, blank=True, null=True)
    fk_id_orden_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='fk_id_orden_compra', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Habitacion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    numero_habitacion = models.BigIntegerField(blank=True, null=True)
    tipo_cama = models.CharField(max_length=20)
    accesorios = models.CharField(max_length=20)
    precio = models.BigIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'habitacion'


class HabitacionesReserva(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='fk_id_reserva', blank=True, null=True)
    fk_id_huesped = models.ForeignKey('Huesped', models.DO_NOTHING, db_column='fk_id_huesped', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitaciones_reserva'


class Huesped(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    fk_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='fk_id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huesped'


class HuespedesReserva(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='fk_id_reserva', blank=True, null=True)
    fk_id_huesped = models.ForeignKey(Huesped, models.DO_NOTHING, db_column='fk_id_huesped', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huespedes_reserva'


class Menu(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_menu = models.CharField(max_length=20)
    documento_menu = models.BinaryField(blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class OrdenCompra(models.Model):
    id = models.BigIntegerField(primary_key=True)
    monto_pago = models.BigIntegerField(blank=True, null=True)
    fk_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='fk_id_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pedido(models.Model):
    id = models.BigIntegerField(primary_key=True)
    monto_total = models.BigIntegerField()
    estado = models.CharField(max_length=20)
    adjuntar_factura = models.BinaryField(blank=True, null=True)
    fk_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='fk_id_proveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    stock = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    fk_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='fk_id_proveedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductosPedidos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    fk_id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='fk_id_producto', blank=True, null=True)
    fk_id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='fk_id_pedido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_pedidos'


class ProductosSolicitados(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    fk_id_producto = models.ForeignKey('RetiroProducto', models.DO_NOTHING, db_column='fk_id_producto', blank=True, null=True)
    fk_retiro_producto = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_solicitados'


class Proveedor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    rubro = models.CharField(max_length=30)
    numero = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Reserva(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    plantilla_huespedes = models.BinaryField(blank=True, null=True)
    fk_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='fk_id_empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class RetiroProducto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    fk_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='fk_id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retiro_producto'


class Servicio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class ServiciosReserva(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='fk_id_servicio', blank=True, null=True)
    fk_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='fk_id_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_reserva'


class TipoEmpleado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_empleado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'
