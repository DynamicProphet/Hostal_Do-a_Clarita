from django.forms import ModelForm
from django import forms
from .models import *

class MenuForms(forms.ModelForm):
    class Meta:
        model= Menu
        fields = [
            'id',
            'tipo_menu',
            'precio',
            'documento_menu',
        ]
        labels = {
            'id' : 'ID',
            'tipo_menu' : 'Tipo Menu',
            'precio' : 'Precio',
            'documento_menu': 'Adjunto Minuta',
        }

class ReservaForms(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha_inicio',
            'fecha_termino',
            'fk_id_empresa',
        ]
        labels = {
            'id': 'ID',
            'fecha_inicio': 'Fecha Inicio',
            'fecha_termino': 'Fecha Termino',
            'fk_id_empresa': 'ID Empresa',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class':'datepicker'}),
            'fecha_termino': forms.DateTimeInput(attrs={'class':'datepicker'}),
        }