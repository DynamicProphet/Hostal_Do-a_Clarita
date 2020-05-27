#from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

#Para importar el login_required y aplicarlo en el Crud
from django.contrib.auth.decorators import login_required

#Para importar las funciones que estan en views.py
from .views import *

#Para la apis
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import ProductViewSet, ProductViewSetDetail

urlpatterns = [
    path('', home, name='pagina-principal'),
    path('registro/', registro, name='registro'),
    path('quienes-somos/', QuienesSomos, name='quienes-somos'),
    path('realizar-reserva/', RealizarReserva, name='reserva'),
    
    path('comedor/', include([
        path('listar', ComedorListar, name="listar-menu"),
        path('agregar', ComedorAgregar , name="agregar-menu"),
        path('editar/<str:tipo_id>', ComedorEditar, name="editar-menu"),
        path('eliminar/<str:tipo_id>', ComedorEliminar, name="eliminar-menu"),
    ]))
]