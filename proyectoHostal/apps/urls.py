#from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Para importar el login_required y aplicarlo en el Crud
from django.contrib.auth.decorators import login_required

# Para importar las funciones que estan en views.py
from .views import *


urlpatterns = [
    path('', home, name='pagina-principal'),
    path('registracion/', include([
        path('registro-usuario-django/',
             RegistroUsuario.as_view(), name='registro-usuario'),
        path('registro/', RegistroUsuarioV2, name='registro'),
        path('registro_exitoso/', RegistroExitoso, name='registro_exitoso'),
    ])),
    path('quienes-somos/', QuienesSomos, name='quienes-somos'),
    path('reserva/', include([
         path('realizar-1', RealizarReserva1, name=""),
         path('realizar-2/<str:f_ini>/<str:f_ter>', RealizarReserva2, name=""),
         path('validar/<int:id>/<int:cant_hab>/<str:f_ini>/<str:f_ter>',
              ReservaValidar, name=""),
         path('listar/', ListarReservas, name='listar-reservas'),
         #path('realizar-reserva/', RealizarReserva, name='realizar-reserva'),
         #path('editar/<int:id_reserva>/', EditarReserva, name='editar-reservas'),
         # path('cancelar/<int:id_reserva>/',
         #     CancelarReserva, name='cancelar-reservas'),
         # path('registrar-habitacion-reserva/', RegistrarHabitacionReserva,
         #     name='registrar-habitacion-reserva'),
         path('ver-estado-reserva/<int:id_reserva>/',
              VerEstadoReserva, name='ver-estado-reserva'),
         path('realizar-pago/<int:id_reserva>/',
              PagarReserva, name='pagar-reserva'),
         ])),
    path('habitacion/', include([
        path('habitacion-agregar/', AgregarHabitacion, name='habitacion-agregar'),
        path('habitacion-listar/', ListarHabitacion, name='habitacion-listar'),
        path('editar/<int:id_habitacion>/',
             EditarHabitacion, name='editar-habitacion')
    ])),
    path('comedor/', include([
        path('listar', ComedorListar, name="listar-menu"),
        path('agregar', ComedorAgregar, name="agregar-menu"),
        path('adjunto/<int:menu_id>', ComedorAdjunto, name="adjunto-menu"),
        path('editar/<int:menu_id>', ComedorEditar, name="editar-menu"),
        path('eliminar/<int:menu_id>', ComedorEliminar, name="eliminar-menu"),
    ])),
    path('producto/', include([
        path('listar', ProductoListar, name="listar-producto"),
        path('agregar', ProductoAgregar, name="agregar-producto"),
        path('editar/<int:prod_id>', ProductoEditar, name="editar-producto"),
        #path('eliminar/<int:prod_id>', ProductoEliminar, name="eliminar-producto"),
        path('id_fk_id_tipo/', include([
            path('agregar', TipoProductoAgregar, name="agregar-tipo-producto"),
            path('editar/<int:prod_tipo_id>', TipoProductoEditar,
                 name="editar-tipo-producto"),
            #path('eliminar/<int:prod_tipo_id>', TipoProductoEliminar, name="eliminar-producto"),
        ])),
        path('id_fk_id_marca/', include([
            path('agregar', MarcaProductoAgregar,
                 name="agregar-marca-producto"),
            path('editar/<int:prod_marca_id>', MarcaProductoEditar,
                 name="editar-marca-producto"),
            #path('eliminar/<int:prod_marca_id>', MarcaProductoEliminar, name="eliminar-producto"),
        ])),
    ])),
    path('retiro-producto/', include([
        path('listar', RetiroProductoListar, name="listar-retiro-producto"),
        path('agregar/<int:emp_rut>', RetiroProductoAgregar,
             name="agregar-retiro-producto"),
        path('eliminar/<int:id>', RetiroProductoEliminar,
             name="eliminar-retiro-producto"),
        path('finalizar/<int:id_RP>', FinalizarRP,
             name="elifinalizar-retiro-producto"),
    ])),
    path('solicitud-producto/', include([
        path('listar/<int:id_RP>', ProductoSolicitadoListar,
             name="listar-solicitud-producto"),
        path('agregar/<int:id_RP>', ProductoSolicitadoAgregar,
             name="agregar-solicitud-producto"),
        path('editar/<int:id_PS>', ProductoSolicitadoEditar,
             name="editar-solicitud-producto"),
        path('eliminar/<int:id_PS>', ProductoSolicitadoEliminar,
             name="eliminar-solicitud-producto"),
    ])),
    path('proveedor/', include([
        path('listar/', ListarProveedor, name="listar-proveedor"),
        path('agregar/', AgregarProveedor, name="agregar-proveedor"),
        path('editar/<int:id_proveedor>/',
             ModificarProveedor, name="editar-proveedor"),
        path('eliminar/<int:id_proveedor>/',
             EliminarProveedor, name="eliminar-proveedor"),
    ])),
    path('adm_huespedes/', include([
        path('listar/<int:id_res>/<int:isPagada>', AdmHuespedesListar,
             name="listar-adm-huesped"),
    ])),
    path('pedido/', include([
        path('listar/', ListarPedido, name="listar-pedido"),
        path('agregar/<int:id_proveedor>/',
             AgregarPedido, name="agregar-pedido"),
        path('editar/<int:id_pedido>/', ModificarPedido, name="editar-pedido"),
        path('recibir/<int:id_pedido>/', RecibirPedido, name="recibir-pedido"),
        path('agregar/<int:id_proveedor>/productos/<int:id_pedido>/',
             AgregarProductosPedido, name="agregar-productos_pedido"),
        path('listado-productos/<int:id_pedido>/',
             ListarProductosPedido, name="listado-productos-pedido"),
        path('listado-productos/<int:id_pedido>/eliminar/<int:id_prod_pedido>/',
             EliminarProductosPedido, name="eliminar-productos-pedido"),
        path('listado-productos/<int:id_pedido>/modificar/<int:id_prod_pedido>/',
             ModificarProductoPedido, name="modificar-productos-pedido"),
    ])),
    path('orden/', include([
        path('listar', OrdenListar, name="listar-orden"),
        path('ver/<int:id>', OrdenVer, name="ver-orden"),
    ])),
    path('informe/', include([
        path('crear', InformeCrear, name="crear-informe"),
        path('facturas', InformeCrearFacuras, name="facturas-informe"),
        path('ExcelFac', ExcelFacturas, name="facturas-excel"),
    ])),
    path('adm_habitaciones/', include([
        path('administracion-habitaciones/', AdministracionHabitaciones,
             name="administrar-habitaciones"),
    ])),
    path('reserva2/', include([
        path('', RealizarReserva1, name=""),
        path('realizar/<str:f_ini>/<str:f_ter>', RealizarReserva2, name=""),
        path('validar/<int:id>/<int:cant_hab>/<str:f_ini>/<str:f_ter>',
             ReservaValidar, name=""),
    ])),

    path('check/', include([
        path('in/<int:id_hab>', CheckIn, name=""),
        path('out/<int:id_res>', CheckOut, name=""),
    ])),

    path('servicio/', include([
        path('listar/<int:id_reserva>/', Servicios, name=""),
    ])),
]
