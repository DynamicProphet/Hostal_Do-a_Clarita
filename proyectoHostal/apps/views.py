from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

#CU13: Administrar La Página
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

def VerReservas(request):
    reservas = Reserva.objects.all().order_by('id')
    user = request.user
    if False: #Valida si el usuario es de tipo cliente
        return render(request, 'reserva/ver_reservas.html', {})
    elif True: #Valida si el usuario es de tipo empleado
        return render(request, 'reserva/ver_reservas.html', {'reservas': reservas})
    else:
        return redirect('/')
    

#CU6: Administrar Comedor
def ComedorListar(request):
    menus = Menu.objects.all()
    return render(request, 'Cocina/menu_listar.html', {'menus' : menus}) 

def ComedorAgregar(request):
    if request.method == 'POST':
        form = MenuForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            tipo_menu = form.cleaned_data.get('tipo_menu')
            messages.success(request, f'El Menu {tipo_menu} Se Ha Agregado!')
            return redirect('/comedor/listar')
    else:
        form = MenuForms()
    return render(request, 'Cocina/agregar_listar.html', {}) 

def ComedorEditar(request,menu_id):
    instancia= Menu.objects.get(id=menu_id)
    form=  MenuForms(instance=instancia)
    if request.method=="POST":
        form= MenuForms(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
            tipo_menu = form.cleaned_data.get('tipo_menu')
            messages.success(request, f'El Menu {tipo_menu} Se Ha Agregado!')
            return redirect('/comedor/listar')
    return render(request, 'Cocina/editar_listar.html', {}) 

def ComedorEliminar(request,menu_id):
    instacia= Menu.objects.get(id=menu_id)
    instacia.delete()
    messages.warning(request, f'El Menu {instacia.tipo_menu} Se Ha Eliminado!')
    return redirect('/comedor/listar') 