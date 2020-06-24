#from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

#Para importar el login_required y aplicarlo en el Crud
from django.contrib.auth.decorators import login_required

#Para importar las funciones que estan en views.py
from .views import *


urlpatterns = [
    path('', home, name='pagina-principal'),
    path('registracion/', include([
        path('registro-usuario-django/', RegistroUsuario.as_view(), name='registro-usuario'),
        path('registro/', RegistroUsuarioV2, name='registro'),
        path('registro_exitoso/', RegistroExitoso, name='registro_exitoso'),            
    ])),
    path('quienes-somos/', QuienesSomos, name='quienes-somos'),
    path('reserva/', include ([
        path('realizar-reserva/', RealizarReserva, name='realizar-reserva'),
        path('listar/', ListarReservas, name='listar-reservas'),
        path('editar/<int:id_reserva>/', EditarReserva, name='editar-reservas'),
        path('cancelar/<int:id_reserva>/', CancelarReserva, name='cancelar-reservas'),
        path('registrar-habitacion-reserva/', RegistrarHabitacionReserva, name='registrar-habitacion-reserva'),
        path('realizar-pago/<int:id_reserva>/', PagarReserva, name='pagar-reserva'),
        path('pago-exitoso/', PagoExitoso, name='pago-exitoso'),
    ])),
    path('habitacion/', include([
        path('habitacion-agregar/', AgregarHabitacion, name='habitacion-agregar'),
        path('habitacion-listar/', ListarHabitacion, name='habitacion-listar'),
        path('editar/<int:id_habitacion>/', EditarHabitacion, name='editar-habitacion')
    ])),
    path('comedor/', include([
        path('listar', ComedorListar, name="listar-menu"),
        path('agregar', ComedorAgregar , name="agregar-menu"),
        path('adjunto/<int:menu_id>', ComedorAdjunto, name="adjunto-menu"),
        path('editar/<int:menu_id>', ComedorEditar, name="editar-menu"),
        path('eliminar/<int:menu_id>', ComedorEliminar, name="eliminar-menu"),
    ])),
    path('producto/', include([
        path('listar', ProductoListar, name="listar-producto"),
        path('agregar', ProductoAgregar , name="agregar-producto"),
        path('editar/<int:prod_id>', ProductoEditar, name="editar-producto"),
        path('eliminar/<int:prod_id>', ProductoEliminar, name="eliminar-producto"),
        path('id_fk_id_tipo/', include([
            path('agregar', TipoProductoAgregar , name="agregar-tipo-producto"),
            path('editar/<int:prod_tipo_id>', TipoProductoEditar, name="editar-tipo-producto"),
            path('eliminar/<int:prod_tipo_id>', TipoProductoEliminar, name="eliminar-producto"),
        ])),
        path('id_fk_id_marca/', include([
            path('agregar', MarcaProductoAgregar , name="agregar-marca-producto"),
            path('editar/<int:prod_marca_id>', MarcaProductoEditar, name="editar-marca-producto"),
            path('eliminar/<int:prod_marca_id>', MarcaProductoEliminar, name="eliminar-producto"),
        ])),
    ])),
]