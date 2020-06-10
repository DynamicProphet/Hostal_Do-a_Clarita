from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MenuForms(forms.ModelForm):
    class Meta:
        model= Menu
        fields = [
            'tipo_menu',
            'precio',
            'documento_menu',
        ]
        labels = {
            'tipo_menu' : 'Tipo Menu',
            'precio' : 'Precio',
            'documento_menu': 'Adjunto Minuta',
        }
        widgets = {
            'tipo_menu' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'documento_menu' : forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

class ReservaForms(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha_inicio',
            'fecha_termino',
            'plantilla_huespedes',
            'fk_id_empresa',
        ]
        labels = {
            'id': 'ID',
            'fecha_inicio': 'Fecha Inicio',
            'fecha_termino': 'Fecha Termino',
            'plantilla_huespedes': 'Plantilla de Huespedes',
            'fk_id_empresa': 'ID Empresa',
        }
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control', "placeholder" : "aaaa-mm-dd", "style": "text-align:center"}),
            'fecha_termino': forms.TextInput(attrs={'class': 'form-control', "placeholder" : "aaaa-mm-dd", "style": "text-align:center"}),
        }
        

class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'email',
		]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'email': 'Correo',
		}

#CU1
class RegistroForms(forms.ModelForm):
    class Meta:
        model= Empresa
        fields = [
            'rut',
            'nombre',
            'email',
            'numero',
        ]
        labels = {
            'rut' : 'Rut',
            'nombre' : 'Nombre',
            'email' : 'Email',
            'numero' : 'Numero',
        }
        widgets = {
            'rut' : forms.TextInput(attrs={'class': 'form-control', "placeholder" : "Poner rut sin puntos ni guion, Ejemplo: 205461239"}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'numero' : forms.TextInput(attrs={'class': 'form-control', "placeholder" : "Ejemplo: +56975486232"}),
        }

class AgregarHabitacionForms(forms.ModelForm):
    class Meta:
        model= Habitacion
        fields = [
            'numero_habitacion',
            'tipo_cama',
            'accesorios',
            'precio',
            'estado',
        ] 
        labels = {
            'numero_habitacion' : 'Numero de habitacion',
            'tipo_cama' : 'Tipo de cama',
            'accesorios' : 'Accesorios',
            'precio' : 'Precio',
            'estado' : 'Estado',
        }   
        widgets = {
            'numero_habitacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cama' : forms.TextInput(attrs={'class': 'form-control', "placeholder" : "Plaza, Plaza y media, Dos plazas, King, Super king", "style": "text-align:center"}),
            'accesorios' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'estado' : forms.TextInput(attrs={'class': 'form-control', "placeholder" : "Reservada, Disponible, Mantenimiento", "style": "text-align:center"}),
        }

class HabitacionForms(forms.ModelForm):
    class Meta:
        model= Habitacion
        fields = [
            'numero_habitacion',
            'tipo_cama',
            'accesorios',
            'precio',
            'estado',
        ] 
        labels = {
            'numero_habitacion' : 'Numero de habitacion',
            'tipo_cama' : 'Tipo de cama',
            'accesorios' : 'Accesorios',
            'precio' : 'Precio',
            'estado' : 'Estado',
        }   

