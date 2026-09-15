from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'rut',
        'username', 
        'first_name', 
        'last_name',
        'email',  
        'telefono', 
        'direccion',
        'is_staff'
    )
    
    list_filter = (
        'is_staff',
        'last_name'
    )
    
    search_fields = (
        'rut',
        'username',
        'last_name'
    )

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'numero_cuenta', 
        'tipo_cuenta', 
        'saldo'
    )
    
    list_filter = (
        'cliente',
        'tipo_cuenta'
    )
    
    search_fields = (
        'cliente',
        'numero_cuenta'
    )


@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'nombre', 
        'rut', 
        'email',
        'cuenta',
        'banco'
    )
    
    list_filter = (
        'banco',
    )
    
    search_fields = (
        'nombre', 
        'rut'
    )

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = (
        'cuenta',
        'tipo_transaccion', 
        'banco_destino', 
        'monto',
        'destinatario',
        'fecha'
    )
    
    list_filter = (
        'banco_destino',
        'tipo_transaccion',
        'fecha'

    )
    
    search_fields = (
        'cuenta', 
        'destinatario'
    )