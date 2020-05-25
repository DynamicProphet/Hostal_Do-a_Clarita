from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    contenidos = ContenidoWeb.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})

def registro(request):
    #Falta llenar
    return render(request, 'registration/registro.html', {})

def QuienesSomos(request):
    #Falta llenar
    return render(request, 'quienes_somos.html', {})

def RealizarReserva(request):
    #Falta llenar
    return render(request, 'reserva/realizar_reserva.html', {})
