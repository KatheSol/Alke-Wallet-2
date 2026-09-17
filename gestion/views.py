from django.shortcuts import render

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
    return render(request, "gestion/user/transacciones_cliente.html")

def envio_dinero(request):
    return render(request, "gestion/user/envio_dinero.html")

def deposito(request):
    return render(request, "gestion/user/deposito.html")

def dashboard_admin(request):
    return render(request,"gestion/administrador/dashboard_admin.html")

def transacciones(request):
    return render(request, "gestion/administrador/transacciones.html")

def lista_clientes(request):
    return render(request, "gestion/administrador/lista_clientes.html")

def datos_cliente(request):
    return render(request, "gestion/administrador/datos_cliente.html")