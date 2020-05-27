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