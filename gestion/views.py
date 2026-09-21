import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "gestion/index/index.html")

def login_cliente(request):
    return render(request, "gestion/index/login.html")

### registro cliente
def registro(request):

    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False) ###guardar temporalmente
            cliente.username = cliente.rut
            cliente.save() ### se guarda
            login(request,cliente)

            ###Creamos una cuenta bancaria cuando se registre un cliente
            # rescatamos el tipo de cuenta seleccionada
            cuenta_select = form.cleaned_data.get('tipo_cuenta')
            
            # creamos el numero aleatorio de la cuenta
            while True:
                nro_aleatorio = str(random.randint(1000000000, 9999999999))
                if not Cuenta.objects.filter(numero_cuenta=nro_aleatorio).exists():
                    break # sale del bucle cuando encuentra un número disponible

            # se crea la cuenta bancaria cliente
            Cuenta.objects.create(
                cliente=cliente, 
                numero_cuenta=nro_aleatorio,
                tipo_cuenta=cuenta_select
                )
            
            return redirect('dashboard-cliente')
            
    
        else: 
            return render(request,"gestion/index/registro_user.html", {'form':form})

    else:
        form = ClienteForm()

    return render(request, 'gestion/index/registro_user.html', {'form':form})


def dashboard_cliente(request):
    return render(request,"gestion/user/dashboard_cliente.html")

def transacciones_cliente(request):
    ## CAMBIAR A FILTER(cliente=pk)
    transacciones = Transaccion.objects.all().select_related('destinatario').select_related('cliente')
    ### Si existen transacciones registradas envía datos
    if len(transacciones)>0:
        return render(request, "gestion/user/transacciones_cliente.html", {'transacciones':transacciones})
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/user/transacciones_cliente.html")

def envio_dinero(request):
    return render(request, "gestion/user/envio_dinero.html")

def deposito(request):
    return render(request, "gestion/user/deposito.html")

def dashboard_admin(request):
    return render(request,"gestion/administrador/dashboard_admin.html")

def transacciones(request):

    transacciones = Transaccion.objects.all().select_related('destinatario','cuenta')
    
    ### Si existen transacciones registradas envía datos
    if len(transacciones)>0:
        return render(request, "gestion/administrador/transacciones.html", {'transacciones':transacciones})
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/administrador/transacciones.html")

#### muestra la lista de clientes
def lista_clientes(request):

    if request.method =='POST':

        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False) ###guardar temporalmente
            cliente.username = cliente.rut
            cliente.save() ### se guarda

            ###Creamos una cuenta bancaria cuando se registre un cliente
            # rescatamos el tipo de cuenta seleccionada
            cuenta_select = form.cleaned_data.get('tipo_cuenta')
            
            # creamos el numero aleatorio de la cuenta
            while True:
                nro_aleatorio = str(random.randint(1000000000, 9999999999))
                if not Cuenta.objects.filter(numero_cuenta=nro_aleatorio).exists():
                    break # sale del bucle cuando encuentra un número disponible

            # se crea la cuenta bancaria cliente
            Cuenta.objects.create(
                cliente=cliente, 
                numero_cuenta=nro_aleatorio,
                tipo_cuenta=cuenta_select
                )
            
            return redirect('lista-clientes')          
        
        else: 
            return render(request, "gestion/administrador/lista_clientes.html")

    else:
        form = ClienteForm()

    cuentas = Cuenta.objects.all().select_related('cliente')
    ### Si existen cuentas registradas envía datos
    if len(cuentas)>0:
        return render(request, "gestion/administrador/lista_clientes.html",{
            'cuentas':cuentas,
            'form': form
            })
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/administrador/lista_clientes.html")

def datos_cliente(request,pk):

    cliente = get_object_or_404(Cliente, pk=pk)
    cuentas = Cuenta.objects.filter(cliente_id=cliente)
    transacciones = Transaccion.objects.filter(cuenta__cliente=cliente).select_related('cuenta')
    ultimos_movimientos = Transaccion.objects.filter(cuenta__cliente=cliente).select_related('cuenta').order_by('-fecha')[:5]
    return render(request, "gestion/administrador/datos_cliente.html", {
        'cliente': cliente,
        'cuentas': cuentas,
        'transacciones': transacciones,
        'ultimos_movimientos': ultimos_movimientos
    })