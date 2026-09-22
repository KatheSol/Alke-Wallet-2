from django import forms
from .models import *
##### login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## Formulario para Agregar cliente
class ClienteForm(forms.ModelForm):

    TIPO_CUENTA = [
        ('vista', 'Cuenta vista'),
        ('ahorro', 'Cuenta ahorro'),
        ('corriente', 'Cuenta corriente')
    ]

    # Selecct tipo cuenta
    tipo_cuenta = forms.ChoiceField(
        choices=TIPO_CUENTA,
        label="Tipo de Cuenta",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Cliente
        fields = ['rut','first_name','last_name','password', 'email','direccion', 'telefono']
        widgets = {   
            'rut':forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control',}
            ),
            'password': forms.TextInput(
                attrs={'class':'form-control', 'type':'password'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control', 'type':'email'}
            ),
            'direccion': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'telefono': forms.TextInput(
                attrs={'class':'form-control'}
            ),
        }
        labels = {
            'rut': 'RUT:',
            'first_name': 'Nombre:',
            'last_name': 'Apellido:',
            'password': 'Contraseña:',
            'email': 'Email:',
            'direccion': 'Dirección',
            'telefono': 'Teléfono:',
        }
        
        def clean_rut(self):
            rut = self.cleaned_data['rut']
            if len(rut) < 9:
                raise forms.ValidationError("Debe ingresar un rut válido")
            return rut

    ### para que el select de tipo de cuenta quede al inicio
    field_order = ['tipo_cuenta','rut','first_name','last_name','password', 'email','direccion', 'telefono']

## Formulario para editar cliente
class EditarClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['rut','first_name','last_name','email','direccion','telefono']
        widgets = {   
            'rut':forms.TextInput(
                attrs={'class':'form-control input-claro', 'readonly':True}
            ),
            'first_name': forms.TextInput(
                attrs={'class':'form-control input-claro'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control input-claro',}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control input-claro', 'type':'email'}
            ),
            'direccion': forms.TextInput(
                attrs={'class':'form-control input-claro'}
            ),
            'telefono': forms.TextInput(
                attrs={'class':'form-control input-claro'}
            ),
        }
        labels = {
            'rut': 'RUT:',
            'first_name': 'Nombre:',
            'last_name': 'Apellido:',
            'email': 'Email:',
            'direccion': 'Dirección',
            'telefono': 'Teléfono:',
        }
        