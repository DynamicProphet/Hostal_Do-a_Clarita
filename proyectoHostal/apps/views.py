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
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
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

def VerEstadoReserva(request, id_reserva):
    orden_compra = OrdenCompra.objects.all().filter(fk_id_reserva=id_reserva)
    facturas = Factura.objects.all()
    isPagada = True
    idReserva = id_reserva 
    for orden in orden_compra:
        orden_id = str(orden.id)
    for factura in facturas:
        fact = str(factura.fk_id_orden_compra)
        if fact != orden_id:
            isPagada = False
        else:
            isPagada = True
            break
    return render(request, 'reserva/ver_estado_reserva.html', {'orden_compra':orden_compra, 'facturas':facturas, 'isPagada': isPagada, 'idReserva': idReserva })

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
                messages.success(request, f'El Menu {tipo_menu} Se Ha Editado!')
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
    habitaciones_reserva = HabitacionesReserva.objects.all().filter(fk_id_reserva=id_reserva)
    facturas = Factura.objects.all()
    idReserva = id_reserva
    if request.user.groups.filter(name = "SECRETARIA" ).exists():
        if request.method == 'POST':
            form = FacturaForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/reserva/ver-estado-reserva/'+str(id_reserva)+'/')
        else:
            form = FacturaForms()
        return render(request, "reserva/pago_reserva.html", {'orden_compras': orden_compras, 'servicios_reservas' :servicios_reservas, 'habitaciones_reserva': habitaciones_reserva, 'idReserva': idReserva, 'forms': forms})
    else:
        return redirect('/')

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

#tipo
def TipoProductoAgregar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Agregar'
        if request.method == 'POST':
            form = TipoProductoForm(request.POST)
            if form.is_valid():
                form.save()            
                prod_nombre = form.cleaned_data.get('nombre')
                messages.success(request, f'El Tipo Producto {prod_nombre} Se Ha Agregado!')
                next = request.POST.get('next','/')
                return HttpResponseRedirect(next)
        else:
            form = TipoProductoForm()
        return render(request, 'producto/cu-tipo-producto.html', {'form': form,'tipo':tipo})
    return redirect('/')

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
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
        return render(request, 'producto/cu-tipo-producto.html', {'form': form,'tipo':tipo})
    return redirect('/')

def TipoProductoEliminar(request,prod_tipo_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instacia= TipoProducto.objects.get(id=prod_tipo_id)
        instacia.delete()
        messages.warning(request, f'El Tipo Producto {instacia.descripcion} Se Ha Eliminado!')
        return redirect(request.META['HTTP_REFERER']) 
    return redirect('/')
#marca
def MarcaProductoAgregar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        tipo = 'Agregar'
        if request.method == 'POST':
            form = MarcaForm(request.POST)
            if form.is_valid():
                form.save()            
                descripcion = form.cleaned_data.get('descripcion')
                messages.success(request, f'La Marca {descripcion} Se Ha Agregado!')
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
        else:
            form = MarcaForm()
        return render(request, 'producto/cu-marca-producto.html', {'form': form,'tipo':tipo})
    return redirect('/')

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
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
        return render(request, 'producto/cu-marca-producto.html', {'form': form,'tipo':tipo})
    return redirect('/')

def MarcaProductoEliminar(request,prod_marca_id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instacia= MarcaProducto.objects.get(id=prod_marca_id)
        instacia.delete()
        messages.warning(request, f'La Marca {instacia.descripcion} Se Ha Eliminado!')
        return redirect(request.META['HTTP_REFERER'])
    return redirect('/')

#Retiro Producto
def RetiroProductoListar(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        retiroproducto = RetiroProducto.objects.all().order_by('-id')
        empleados = Empleado.objects.all()
        return render(request, 'retiro_producto/listar-retiro.html', {'retiroproducto' : retiroproducto,'empleados':empleados}) 

def RetiroProductoAgregar(request,emp_rut):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        emp = Empleado.objects.get(rut=emp_rut)
        rp = RetiroProducto(finalizada=0,fk_id_empleado=emp)
        rp.save()
        messages.success(request, f'Retiro De Producto Para El Empleado {emp.nombre} Agregado!, Favor de Asignar Productos!')
        return redirect(request.META['HTTP_REFERER'])
    return redirect('/')

def RetiroProductoEliminar(request,id):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        #producto solicitados asociados al retiro
        productos = ProductosSolicitados.objects.all().filter(fk_retiro_producto=id)
        for x in productos:
            x.delete() 
        #Eliminar Retiro
        instacia= RetiroProducto.objects.get(id=id)
        instacia.delete()
        messages.warning(request, f'Retiro De Producto Eliminado!')
        return redirect('/retiro-producto/listar') 
    return redirect('/')

#Producto Solicitado
def ProductoSolicitadoListar(request,id_RP):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        productos = ProductosSolicitados.objects.all().filter(fk_retiro_producto=id_RP)
        retiro_prod = RetiroProducto.objects.get(id=id_RP)
        RP_F = retiro_prod.finalizada
        return render(request, 'retiro_producto/producto_solicitado/listar-producto-solicitud.html', {'productos' : productos,'id_RP':id_RP,'RP_F':RP_F}) 
    return redirect('/producto/listar')

def ProductoSolicitadoAgregar(request,id_RP):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        productos = Producto.objects.all().values_list('id','stock')
        prod_json = json.dumps(list(productos), cls=DjangoJSONEncoder)
        if request.method == 'POST':
            form = ProductosSolicitadosForm(request.POST)
            if form.is_valid():
                form.save()            
                messages.success(request, f'El Producto Se Ha Agregado!')
                next = request.POST.get('next','/')
                return HttpResponseRedirect(next)
        else:
            form = ProductosSolicitadosForm()
        return render(request, 'retiro_producto/producto_solicitado/agregar-producto-solicitud.html', {'form': form,'id_RP':id_RP,'productos':prod_json})
    return redirect('/')

def ProductoSolicitadoEditar(request,id_PS):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        productos = Producto.objects.all().values_list('id','stock')
        prod_json = json.dumps(list(productos), cls=DjangoJSONEncoder)
        instancia= ProductosSolicitados.objects.get(id=id_PS)
        form=  ProductosSolicitadosForm(instance=instancia)
        if request.method=="POST":
            form= ProductosSolicitadosForm(request.POST, instance=instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                messages.success(request, f'El Producto Se Ha Editado!')
                next = request.POST.get('next','/')
                return HttpResponseRedirect(next)
        return render(request, 'retiro_producto/producto_solicitado/editar-producto-solicitud.html', {'form': form,'productos':prod_json})
    return redirect('/')

def ProductoSolicitadoEliminar(request,id_PS):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        instacia= ProductosSolicitados.objects.get(id=id_PS)
        instacia.delete()
        messages.warning(request, f'El Producto Se Ha Eliminado!')
        return redirect(request.META['HTTP_REFERER']) 
    return redirect('/')

#Finalizar Retiro Producto
def FinalizarRP(request,id_RP):
    if request.user.groups.filter(name = "EMPLEADO BODEGA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        SP = ProductosSolicitados.objects.all().filter(fk_retiro_producto=id_RP)
        retiro_prod = RetiroProducto.objects.get(id=id_RP)
        retiro_prod.finalizada = 1
        retiro_prod.save()
        
        for x in SP:
            Prod = Producto.objects.get(id=x.fk_id_producto.id)
            Prod.stock = Prod.stock - x.cantidad
            Prod.save()
            messages.warning(request, f'Se Han Descontado {x.cantidad} Unidades Al Producto {Prod.nombre}, El Stock Actual es de {Prod.stock}')
        return redirect('/retiro-producto/listar')

#Cu9 Ordenes de Pedido(Proveedores)

def AgregarProveedor(request):
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists():
        if request.method == 'POST':
            form = ProveedorForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/proveedor/listar/')
        else:
            form = ProveedorForms()
        return render(request, 'proveedor/agregar_proveedor.html', {'form':form})
    else:
        return redirect('/')

def EliminarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists():
        if request.method == 'POST':
            proveedor.delete()
            return redirect('/proveedor/listar/')
        return render(request, 'proveedor/eliminar_proveedor.html', {'proveedor': proveedor})
    else:
        return redirect('/')
    

def ListarProveedor(request):
    proveedores = Proveedor.objects.all().order_by('id')
    if  request.user.groups.filter(name='EMPLEADO BODEGA').exists():
        return render(request, 'proveedor/listar_proveedor.html', {'proveedores': proveedores})
    else:
        return redirect('/')

def ModificarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    user = request.user
    if request.user.groups.filter(name = 'EMPLEADO BODEGA').exists():
        if request.method == "GET":
            form = ProveedorForms(instance=proveedor)
        else:
            form = ProveedorForms(request.POST, instance=proveedor)
            if form.is_valid():
                proveedor = form.save(commit=False)
                proveedor.save()
            return redirect('/proveedor/listar/')
        return render(request, 'proveedor/modificar_proveedor.html', {'form': form} )
    else:
        return redirect('/') 
        #return redirect('/retiro-producto/listar') 
    return redirect('/')

#CU5: Administracion Huepedes
def AdmHuespedesListar(request,id_res):
    if request.user.groups.filter(name = "SECRETARIA" ).exists() or request.user.groups.filter(name = "ADMINISTRADOR" ).exists() or request.user.is_superuser:
        HR = HuespedesReserva.objects.all().filter(fk_id_reserva=id_res)
        reserva = Reserva.objects.get(id=id_res)
        return render(request, 'adm_huespedes/adm_huespedes_listar.html', {'HR':HR,'reserva':reserva}) 
    return redirect('/')

#CU9: Ordenes de Pedido(Pedidos)

def AgregarPedido(request, id_proveedor):
    productos = Producto.objects.all().filter(fk_id_proveedor=id_proveedor)
    proveedores = Proveedor.objects.all().filter(id=id_proveedor)
    pedidos = Pedido.objects.all().order_by('-id')
    idProveedor = id_proveedor

    for pedido in pedidos:
        idPedido = pedido.id + 1
        break
    
    print(idPedido)
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists():
        if request.method == 'POST':
            form = PedidoForms(request.POST)
            if form.is_valid():
                form.save()
                urlReturn = '/pedido/agregar/' + str(idProveedor) + '/productos/' + str(idPedido) + '/'
            return redirect(urlReturn)
        else:
            form = PedidoForms()
        return render(request, 'pedido/agregar_pedido.html', {'form':form, 'productos': productos, 'proveedores': proveedores, 'idProveedor': idProveedor, 'idPedido': idPedido})
    else:
        return redirect('/')

def AgregarProductosPedido(request, id_proveedor, id_pedido):
    productos = Producto.objects.all().filter(fk_id_proveedor=id_proveedor)
    proveedores = Proveedor.objects.all().filter(id=id_proveedor)
    idPedido = id_pedido
    if request.user.groups.filter(name = "EMPLEADO BODEGA").exists():
        if request.method == 'POST':
            print("1")
            form = ProductosPedidoForms(request.POST)
            print(form.is_valid())
            if form.is_valid():
                print("Llega!!")
                form.save()
            #return redirect('/pedido/listar/')
        else:
            form = ProductosPedidoForms()
        return render(request, 'pedido/agregar_productos_pedido.html', {'form':form, 'productos': productos, 'proveedores': proveedores, 'idPedido': idPedido})
    else:
        return redirect('/')
    

def ListarPedido(request):
    pedidos = Pedido.objects.all().order_by('id')
    proveedores = Proveedor.objects.all()
    if  request.user.groups.filter(name='EMPLEADO BODEGA').exists():
        return render(request, 'pedido/listar_pedido.html', {'pedidos': pedidos, 'proveedores': proveedores})
    else:
        return redirect('/')

def ModificarPedido(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    user = request.user
    if request.user.groups.filter(name = 'EMPLEADO BODEGA').exists():
        if request.method == "GET":
            form = PedidoForms(instance=pedido)
        else:
            form = PedidoForms(request.POST, instance=pedido)
            if form.is_valid():
                pedido = form.save(commit=False)
                pedido.save()
            return redirect('/pedido/listar/')
        return render(request, 'pedido/modificar_pedido.html', {'form': form} )
    else:
        return redirect('/')

def RecibirPedido(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    user = request.user
    if request.user.groups.filter(name = 'EMPLEADO BODEGA').exists():
        if request.method == "GET":
            form = PedidoForms(instance=pedido)
        else:
            form = PedidoForms(request.POST, instance=pedido)
            if form.is_valid():
                pedido = form.save(commit=False)
                pedido.save()
            return redirect('/pedido/listar/')
        return render(request, 'pedido/recibir_pedido.html', {'form': form} )
    else:
        return redirect('/')