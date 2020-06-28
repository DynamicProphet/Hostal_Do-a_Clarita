from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
# Create your views here.

#CU13: Administrar La Página
def home(request):
    contenidos = ContenidoWeb.objects.all()
    return render(request, 'home.html', {'contenidos': contenidos})

def RegistroUsuarioV2(request):
    if True:
        if request.method == 'POST':
            form = RegistroEmpresaForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/registracion/registro_exitoso')
        else:
            form = RegistroEmpresaForms()
        return render(request, 'registration/registro.html', {'form': form})
    else:
        return redirect('/')
	
class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro-usuario-django.html"
    form_class = RegistroForms
    success_url = '/registracion/registro/'

#CU1: Registrar
def registro(request):
    if True:
        if request.method == 'POST':
            form = RegistroEmpresaForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/registracion/registro_exitoso')
        else:
            form = RegistroEmpresaForms()
        return render(request, 'registration/registro.html', {'form': form})
    else:
        return redirect('/')

def registroDjango(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Registro de usuario:')
            raw_password = form.cleaned_data.get('Contraseña 1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro-usuario-django.html', {'form': form})

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
    habitacion = Habitacion.objects.get(id=id_habitacion)
    user = request.user
    if request.user.groups.filter(name = "GERENTE" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        if request.method == "GET":
            form = HabitacionForms(instance=habitacion)
        else:
            form = HabitacionForms(request.POST, request.FILES,instance=habitacion)
            if form.is_valid():
                habitacion = form.save(commit=False)
                habitacion.save()
            return redirect('habitacion/habitacion-listar/')
        return render(request, "habitacion/habitacion-listar.html", {'form': form})
    else:
        return redirect('/') 
        
#CU10: Factura
def PagarReserva(request, id_reserva):
    orden_compras = OrdenCompra.objects.all().filter(fk_id_reserva=id_reserva)
    servicios_reservas = ServiciosReserva.objects.all().filter(fk_id_reserva=id_reserva)
    return render(request, "reserva/pago_reserva.html", {'orden_compras': orden_compras, 'servicios_reservas' :servicios_reservas})

def PagoExitoso(request):
    return render(request, "reserva/pago_exitoso.html", {})

#CU11: Administrar Productos
def ProductoListar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        productos = Producto.objects.all()
        return render(request, 'producto/listar-producto.html', {'productos' : productos}) 
    return redirect('/producto/listar')

def ProductoAgregar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        if request.method == 'POST':
            form = ProductoForms(request.POST)
            if form.is_valid():
                form.save()            
                prod_nombre = form.cleaned_data.get('nombre')
                messages.success(request, f'El Producto {prod_nombre} Se Ha Agregado!')
                return redirect('/producto/listar')
        else:
            form = ProductoForms()
        return render(request, 'producto/agregar-producto.html', {'form': form})
    return redirect('/producto/listar')

def ProductoEditar(request,prod_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instancia= Producto.objects.get(id=prod_id)
        form=  ProductoForms(instance=instancia)
        if request.method=="POST":
            form= ProductoForms(request.POST, instance=instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                prod_nombre = form.cleaned_data.get('nombre')
                messages.success(request, f'El Producto {prod_nombre} Se Ha Editado!')
                return redirect('/producto/listar')
        return render(request, 'producto/editar-producto.html', {'form': form,})
    return redirect('/producto/listar')

def ProductoEliminar(request,prod_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instacia= Producto.objects.get(id=prod_id)
        instacia.delete()
        messages.warning(request, f'El Producto {instacia.nombre} Se Ha Eliminado!')
        return redirect('/producto/listar') 
    return redirect('/producto/listar')

def TipoProductoAgregar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Agregar'
        if request.method == 'POST':
            form = TipoProductoForm(request.POST)
            if form.is_valid():
                form.save()            
                prod_nombre = form.cleaned_data.get('nombre')
                messages.success(request, f'El Tipo Producto {prod_nombre} Se Ha Agregado!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = TipoProductoForm()
        return render(request, 'producto/cu-tipo-producto.html', {'form': form,'tipo':tipo})
    return redirect('/producto/listar')

def TipoProductoEditar(request,prod_tipo_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Editar'
        instancia= TipoProducto.objects.get(id=prod_tipo_id)
        form=  TipoProductoForm(instance=instancia)
        if request.method=="POST":
            form= TipoProductoForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                prod_nombre = form.cleaned_data.get('nombre')
                messages.success(request, f'El Tipo Producto {prod_nombre} Se Ha Editado!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'producto/cu-tipo-producto.html', {'form': form,'tipo':tipo})
    return redirect('/producto/listar')

def MarcaProductoAgregar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Agregar'
        if request.method == 'POST':
            form = MarcaForm(request.POST)
            if form.is_valid():
                form.save()            
                descripcion = form.cleaned_data.get('descripcion')
                messages.success(request, f'La Marca {descripcion} Se Ha Agregado!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = MarcaForm()
        return render(request, 'producto/cu-marca-producto.html', {'form': form,'tipo':tipo})
    return redirect('/producto/listar')

def MarcaProductoEditar(request,prod_marca_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Editar'
        instancia= MarcaProducto.objects.get(id=prod_marca_id)
        form=  MarcaForm(instance=instancia)
        if request.method=="POST":
            form= MarcaForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                descripcion = form.cleaned_data.get('descripcion')
                messages.success(request, f'La Marca {descripcion} Se Ha Editado!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'producto/cu-marca-producto.html', {'form': form,'tipo':tipo})
    return redirect('/producto/listar')

def OrdenListar(request):
    ordenes = OrdenCompra.objects.all().order_by('id')
    if request.user.groups.filter(name = "SECRETARIA" ).exists() or request.user.groups.filter(name = "GERENTE" ).exists() or request.user.is_superuser:
        for o in ordenes:
            total = 0
            res = HabitacionesReserva.objects.all().filter(fk_id_reserva=o.fk_id_reserva)
            for r in res:
                hab = Habitacion.objects.all().filter(id=r.fk_id_huesped.id)
                for h in hab:
                    total=total+h.precio
            res2 = ServiciosReserva.objects.all().filter(fk_id_reserva=o.fk_id_reserva)
            for r2 in res2:
                ser = Servicio.objects.all().filter(id=r2.fk_id_servicio.id)
                for s in ser:
                    total=total+s.precio
            o.monto_pago=total
            o.save()
        return render(request, 'orden/orden-listar.html', {'ordenes':ordenes})
    else:
        return redirect('/') 