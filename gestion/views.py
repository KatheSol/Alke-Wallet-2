from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, "gestion/index/index.html")

def login(request):
    return render(request, "gestion/index/login.html")

def registro(request):
    return render(request, "gestion/index/registro_user.html")

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

def lista_clientes(request):

    cuentas = Cuenta.objects.all().select_related('cliente')
    ### Si existen cuentas registradas envía datos
    if len(cuentas)>0:
        return render(request, "gestion/administrador/lista_clientes.html", {'cuentas':cuentas})
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/administrador/lista_clientes.html")

def datos_cliente(request):
    return render(request, "gestion/administrador/datos_cliente.html")