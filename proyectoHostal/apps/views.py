from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import pandas as pd
from django.contrib.auth.models import User
# Create your views here.

#CU13: Administrar La Página
def home(request):
    contenidos = ContenidoWeb.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})

#CU1: Registrar
def registro(request):
    if True:
        if request.method == 'POST':
            form = RegistroForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/registracion/registro_exitoso')
        else:
            form = RegistroForms()
        return render(request, 'registration/registro.html', {'form': form})
    else:
        return redirect('/')

def RegistroExitoso(request):
    return render(request, 'registration/registro_exitoso.html',{})

def QuienesSomos(request):
    #Falta llenar
    return render(request, 'quienes_somos.html', {})

def RealizarReserva(request):
    user = request.user
    if True:
        if request.method == 'POST':
            form = ReservaForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('/')
        else:
            form = ReservaForms()
        return render(request, 'reserva/realizar_reserva.html', {'form': form})
    else:
        return redirect('/')

def RegistrarHabitacionReserva(request):
    return render(request, 'reserva/registrar_habitacion.html', {})

def RegistrarHabitacion(request):
    return render(request, 'reserva/registrar_habitacion.html', {})

def ListarReservas(request):
    reservas = Reserva.objects.all().order_by('id')
    user = request.user
    if  request.user.groups.filter(name='CLIENTE').exists(): #Valida si el usuario es de tipo cliente
        if request.user.first_name != " ":
            empresa = Empresa.objects.get(nombre=request.user.first_name)
            return render(request, 'reserva/ver_reservas.html', {'reservas': reservas, 'empresa': empresa})
        else:
            return render(request, 'reserva/ver_reservas.html', {'reservas': reservas})
    elif request.user.groups.filter(name="SECRETARIA").exists(): #Valida si el usuario es de tipo empleado
        return render(request, 'reserva/ver_reservas.html', {'reservas': reservas})
    else:
        return redirect('/')

def EditarReserva(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    user = request.user
    if request.user.groups.filter(name = "CLIENTE").exists():
        if request.method == "GET":
            form = ReservaForms(instance=reserva)
        else:
            form = ReservaForms(request.POST, request.FILES,instance=reserva)
            if form.is_valid():
                reserva = form.save(commit=False)
                reserva.save()
            return redirect('reserva/ver-reservas/')
        return render(request, "reserva/modificar_reserva.html", {'form': form})
    else:
        return redirect('/') 

def CancelarReserva(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    user = request.user
    if request.user.groups.filter(name = "CLIENTE").exists():
        if request.method == 'POST':
            reserva.delete()
            return redirect('reserva/ver-reservas/')
        return render(request, 'reserva/eliminar_reserva.html', {'reserva': reserva})
    else:
        return redirect('/')
    

#CU6: Administrar Comedor
def ComedorListar(request):
    menus = Menu.objects.all()
    return render(request, 'Cocina/menu_listar.html', {'menus' : menus}) 

def ComedorAgregar(request):
    if request.user.groups.filter(name = "GERENTE COCINA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        if request.method == 'POST':
            form = MenuForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()            
                tipo_menu = form.cleaned_data.get('tipo_menu')
                messages.success(request, f'El Menu {tipo_menu} Se Ha Agregado!')
                return redirect('/comedor/listar')
        else:
            form = MenuForms()
        return render(request, 'Cocina/menu_agregar.html', {'form': form})
    return redirect('/comedor/listar')

def ComedorEditar(request,menu_id):
    if request.user.groups.filter(name = "GERENTE COCINA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
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
        return render(request, 'Cocina/menu_editar.html', {'form': form,})
    return redirect('/comedor/listar')

def ComedorEliminar(request,menu_id):
    if request.user.groups.filter(name = "GERENTE COCINA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instacia= Menu.objects.get(id=menu_id)
        instacia.delete()
        messages.warning(request, f'El Menu {instacia.tipo_menu} Se Ha Eliminado!')
        return redirect('/comedor/listar') 
    return redirect('/comedor/listar')

def ComedorAdjunto(request,menu_id):
    instacia= Menu.objects.get(id=menu_id)
    path = instacia.documento_menu.url
    excel = pd.read_excel(instacia.documento_menu.path)
    excel = excel.fillna('')  
    tabla =  excel.to_html(bold_rows=True,index=False,
    classes="table table-striped table-dark text-light",justify='center')
    return render(request, 'Cocina/menu_adjunto.html', {'tabla':tabla,'path':path}) 

#CU7
def AgregarHabitacion(request):
    User = request.user
    if True:
        if request.method == 'POST':
            form = AgregarHabitacionForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('/habitacion/habitacion-listar')
        else:
            form = AgregarHabitacionForms()
        return render(request, 'habitacion/habitacion-agregar.html',{'form' : form})
    else:
        return redirect('/habitacion/habitacion-listar')

def ListarHabitacion(request):
    habitaciones = Habitacion.objects.all().order_by('id')
    return render(request, 'habitacion/habitacion-listar.html', {'habitaciones': habitaciones})

def EditarHabitacion(request,id):
    if request.user.groups.filter(name = "GERENTE" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instancia = Habitacion.objects.get(id=id)
        form= HabitacionForms(instance=instancia)
        if request.method=="POST":
            form= HabitacionForms(request.POST, request.FILES, instance=instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                return redirect('/habitacion/habitacion-listar')
        return render(request, 'habitacion/habitacion-editar.html', {'form': form})
    return redirect('/habitacion/habitacion-listar/')


