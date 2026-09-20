from django import forms
from .models import *
##### login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## Formulario cliente
class ClienteForm(forms.ModelForm):
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



### Formulario cuenta 
'''class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['cliente', 'numero_cuenta', 'tipo_cuenta','saldo']
        widgets = {
            'cliente':forms.TextInput(
                attrs={'class':'form-control'}
                ),
            'numero_cuenta': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'tipo_cuenta': forms.TextInput(
                attrs={'class':'form-control',}
            ),
            'saldo': forms.DecimalField(
                attrs={'class':'form-control'}
            ),
        }
        labels = {
            'cliente': 'Cliente:',
            'numero_cuenta': 'Numero de cuenta:',
            'tipo_cuenta': 'Tipo de cuenta:',
            'saldo': 'Saldo:',
        }
        
        def clean_cliente(self):
            cliente = self.cleaned_data['cliente']
            if len(cliente) <=0:
                raise forms.ValidationError("El campo cliente no puede estar vacío")
            return cliente

    '''