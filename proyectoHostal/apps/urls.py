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
        path('registro/', registro, name='registro'),
        path('registro_exitoso/', RegistroExitoso, name='registro_exitoso'),            
    ])),
    path('quienes-somos/', QuienesSomos, name='quienes-somos'),
    path('reserva/', include ([
        path('realizar-reserva/', RealizarReserva, name='realizar-reserva'),
        path('listar/', ListarReservas, name='listar-reservas'),
        path('editar/<int:id_reserva>/', EditarReserva, name='editar-reservas'),
        path('cancelar/<int:id_reserva>/', CancelarReserva, name='cancelar-reservas'),
        path('registrar-habitacion/', RegistrarHabitacion, name='registrar-habitacion'),
    ])),
    path('comedor/', include([
        path('listar', ComedorListar, name="listar-menu"),
        path('agregar', ComedorAgregar , name="agregar-menu"),
        path('adjunto/<int:menu_id>', ComedorAdjunto, name="adjunto-menu"),
        path('editar/<int:menu_id>', ComedorEditar, name="editar-menu"),
        path('eliminar/<int:menu_id>', ComedorEliminar, name="eliminar-menu"),
    ])),
]