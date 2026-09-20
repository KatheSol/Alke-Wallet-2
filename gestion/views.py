from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
    return render(request, "gestion/index/index.html")

def login_cliente(request):
    return render(request, "gestion/index/login.html")

def registro(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False) ###guardar temporalmente
            usuario.username = usuario.rut
            usuario.save() ### se guarda
            login(request,usuario)
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
            usuario = form.save(commit=False) ###guardar temporalmente
            usuario.username = usuario.rut
            usuario.save() ### se guarda
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

def datos_cliente(request):
    return render(request, "gestion/administrador/datos_cliente.html")