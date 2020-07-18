from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MenuForms(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'tipo_menu',
            'precio',
            'documento_menu',
        ]
        labels = {
            'tipo_menu': 'Tipo Menu',
            'precio': 'Precio',
            'documento_menu': 'Adjunto Minuta',
        }
        widgets = {
            'tipo_menu': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'documento_menu': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
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
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'fecha_termino': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'plantilla_huespedes': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'fk_id_empresa': forms.Select(attrs={'class': 'form-control col-auto'})
        }
#forms.HiddenInput()

class RegistroForms(UserCreationForm):
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

# CU1


class RegistroEmpresaForms(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'rut',
            'nombre',
            'email',
            'numero',
        ]
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'email': 'Email',
            'numero': 'Numero',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Poner rut de empresa sin puntos ni guion, Ejemplo: 205461239"}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre Empresa"}),
            'email': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Repita el Email"}),
            'numero': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ejemplo: +56975486232"}),
        }


class AgregarHabitacionForms(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = [
            'numero_habitacion',
            'tipo_cama',
            'accesorios',
            'precio',
            'estado',
        ]
        labels = {
            'numero_habitacion': 'Numero de habitacion',
            'tipo_cama': 'Tipo de cama',
            'accesorios': 'Accesorios',
            'precio': 'Precio',
            'estado': 'Estado',
        }
        widgets = {
            'numero_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cama': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Plaza, Plaza y media, Dos plazas, King, Super king", "style": "text-align:center"}),
            'accesorios': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Reservada, Disponible, Mantenimiento", "style": "text-align:center"}),
        }


class HabitacionForms(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = [
            'numero_habitacion',
            'tipo_cama',
            'accesorios',
            'precio',
            'estado',
        ]
        labels = {
            'numero_habitacion': 'Numero de habitacion',
            'tipo_cama': 'Tipo de cama',
            'accesorios': 'Accesorios',
            'precio': 'Precio',
            'estado': 'Estado',
        }

# CU11: Administrar Producto


class ProductoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'stock',
            'nombre',
            'precio',
            'fecha_venc',
            'fk_id_marca',
            'fk_id_tipo',
            'fk_id_proveedor',
        ]
        labels = {
            'id': 'ID',
            'stock': 'Stock',
            'nombre': 'Nombre/Descripcion',
            'precio': 'Precio',
            'fecha_venc': 'Fecha Vencimiento',
            'fk_id_marca': 'Marca',
            'fk_id_tipo': 'Tipo',
            'fk_id_proveedor': 'Proveedor',
        }
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control col-auto'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-auto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control col-auto'}),
            'fecha_venc': forms.SelectDateWidget(attrs={'class': 'form-control col-4'}),
            'fk_id_marca': forms.Select(attrs={'class': 'form-control col-9'}),
            'fk_id_tipo': forms.Select(attrs={'class': 'form-control col-9'}),
            'fk_id_proveedor': forms.Select(attrs={'class': 'form-control col-9'}),
        }


class MarcaForm(forms.ModelForm):
    class Meta:
        model = MarcaProducto
        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Descripcion',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Descripcion',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductosSolicitadosForm(forms.ModelForm):
    class Meta:
        model = ProductosSolicitados
        fields = [
            'fk_id_producto',
            'cantidad',
            'fk_retiro_producto',
        ]
        labels = {
            'fk_id_producto': 'Producto',
            'cantidad': 'Cantidad',
            'fk_retiro_producto': 'Retiro FK',
        }
        widgets = {
            'fk_id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control col-9'}),
            'fk_retiro_producto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class FacturaForms(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'rut_empresa',
            'fk_id_orden_compra',
        ]
        labels = {
            'rut_empresa': 'Rut Empresa',
            'fk_id_orden_compra': 'ID Orden Compra',
        }


class ProveedorForms(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'rubro',
            'numero',
            'email',
        ]
        labels = {
            'nombre': 'Nombre ',
            'rubro': 'Rubro',
            'numero': 'Numero',
            'email': 'Email',
        }


class PedidoForms(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'id',
            'monto_total',
            'estado',
            'adjuntar_factura',
            'fk_id_proveedor',
        ]
        labels = {
            'id': 'ID',
            'monto_total': 'Monto Total',
            'estado': 'Estado',
            'adjuntar_factura': 'Adjuntar Factura',
            'fk_id_proveedor': 'Fk Proveedor',
        }


class ProductosPedidoForms(forms.ModelForm):
    class Meta:
        model = ProductosPedidos
        fields = [
            'cantidad',
            'fk_id_producto',
            'fk_id_pedido',
        ]
        labels = {
            'cantidad': 'Cantidad',
                        'fk_id_producto': 'FK Producto',
                        'fk_id_pedido': 'FK Pedido',
        }


class Reserva1Form(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control col-4'}))
    fecha_termino = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control col-4'}))