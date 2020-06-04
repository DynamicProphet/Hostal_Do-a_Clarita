from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

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
            'fecha_inicio': DateInput(),
            'fecha_termino': DateInput(),
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
 