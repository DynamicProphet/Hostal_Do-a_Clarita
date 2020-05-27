from django.shortcuts import render
from .models import *
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

#CU6: Administrar Comedor
'''def ComedorListar(request):
    menus = Menu.objects.all()
    return render(request, '.html', {'menus' : menus}) 

def ComedorAgregar(request):
    if request.method == 'POST':
        form = #Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            tipo_menu = form.cleaned_data.get('tipo_menu')
            messages.success(request, f'El Menu {tipo_menu} Se Ha Agregado!')
            return redirect('/')
    else:
        form = #Form()
    return render(request, '.html', {}) 

def ComedorEditar(request,menu_id):
    instancia= Menu.objects.get(id=menu_id)
    form=  #Form(instance=instancia)
    if request.method=="POST":
        form= #Form(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
            tipo_menu = form.cleaned_data.get('tipo_menu')
            messages.success(request, f'El Menu {tipo_menu} Se Ha Agregado!')
            return redirect('/')
    return render(request, '.html', {}) 

def ComedorEliminar(request,menu_id):
    instacia= Menu.objects.get(id=menu_id)
    instacia.delete()
    messages.warning(request, f'El Menu {instacia.tipo_menu} Se Ha Eliminado!')
    return render(request, '.html', {}) '''