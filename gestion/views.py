import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "gestion/index/index.html")

### login del usuario
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

#### dashboard para el cliente
def dashboard_cliente(request):
    return render(request,"gestion/user/dashboard_cliente.html")

#### transacciones del cliente
def transacciones_cliente(request):
    ## CAMBIAR A FILTER(cliente=pk)
    transacciones = Transaccion.objects.all().select_related('destinatario').select_related('cliente')
    ### Si existen transacciones registradas envía datos
    if len(transacciones)>0:
        return render(request, "gestion/user/transacciones_cliente.html", {'transacciones':transacciones})
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/user/transacciones_cliente.html")

#### envio de dinero para el cliente
def envio_dinero(request):
    return render(request, "gestion/user/envio_dinero.html")

#### deposito para el cliente
def deposito(request):
    return render(request, "gestion/user/deposito.html")

#### dashboard para el administrador
def dashboard_admin(request):

    ultimos_tramo1 = Transaccion.objects.filter(monto__range=(600000,1500000)).order_by('-fecha')[:5]
    ultimos_tramo2 = Transaccion.objects.filter(monto__gte=0).order_by('-fecha')[:5]

    return render(request,"gestion/administrador/dashboard_admin.html", {
        'ultimos_tramo1': ultimos_tramo1 ,
        'ultimos_tramo2': ultimos_tramo2
    })

#### muestra la lista de todas las transacciones para el administrador
def transacciones(request):

    transacciones = Transaccion.objects.all().select_related('destinatario','cuenta')
    
    ### Si existen transacciones registradas envía datos
    if len(transacciones)>0:
        return render(request, "gestion/administrador/transacciones.html", {'transacciones':transacciones})
    ### sino, muestra solo el html
    else:
        return render(request, "gestion/administrador/transacciones.html")

#### muestra la lista de clientes en sesión administrador
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

            messages.success(request, f"Cliente {cliente.first_name.capitalize()} {cliente.last_name.capitalize()} creado correctamente") 
            
            form = ClienteForm()
            return redirect('lista-clientes')
        
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)          
            

    else:
        form = ClienteForm()

    ##todos los usuarios excepto los admin
    clientes = Cliente.objects.filter(is_staff=0)
    return render(request, "gestion/administrador/lista_clientes.html",{
        'clientes':clientes,
        'form': form
        })

#### muestra el detalle de la información del cliente para el administradors
def datos_cliente(request,pk):

    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method =='POST':
        ### identificamos la accion a realizar
        accion = request.POST.get('accion')

        if accion=='nueva_cuenta':
            tipo_cuenta = request.POST.get('tipo_cuenta')
            ### verificamos si el cliente ya posee una cuenta del tipo escogido
            if Cuenta.objects.filter(cliente=pk,tipo_cuenta=tipo_cuenta).exists():
                messages.error(request, f"Cliente ya posee una cuenta {tipo_cuenta}")

            else:
                # creamos el numero aleatorio de la cuenta
                while True:
                    nro_aleatorio = str(random.randint(1000000000, 9999999999))
                    if not Cuenta.objects.filter(numero_cuenta=nro_aleatorio).exists():
                        break # sale del bucle cuando encuentra un número disponible

                # se crea la cuenta bancaria cliente
                Cuenta.objects.create(
                    cliente=cliente, 
                    numero_cuenta=nro_aleatorio,
                    tipo_cuenta=tipo_cuenta
                    )
            ### volvemos a cargar el formulario con los datos del cliente
            form = EditarClienteForm(instance=cliente)

        elif accion=='cambio_estado':

            cuenta_id = request.POST.get('id_cuenta')
            nuevo_estado = request.POST.get('estado_futuro')

            print(f'{nuevo_estado}-{cuenta_id}')

            cuenta = Cuenta.objects.get(id=cuenta_id)
            cuenta.estado = nuevo_estado
            cuenta.save()
        
            form = EditarClienteForm(instance=cliente)

        ### si no se activa un modal entoces el formulario indica actualizar el cliente
        else:
            ### el instance=cliente es para hacer referencia al cliente seleccionado
            form = EditarClienteForm(request.POST,instance=cliente)
            if form.is_valid():
                cliente = form.save(commit=False) ###guardar temporalmente
                cliente.save() ### se guarda
            else:
                return render(request, "gestion/administrador/datos_cliente.html",{'form': form})
            
    else:
        form = EditarClienteForm(instance=cliente)

    
    cuentas = Cuenta.objects.filter(cliente_id=cliente)
    transacciones = Transaccion.objects.filter(cuenta__cliente=cliente).select_related('cuenta')
    ultimos_movimientos = Transaccion.objects.filter(cuenta__cliente=cliente).select_related('cuenta').order_by('-fecha')[:5]

    return render(request, "gestion/administrador/datos_cliente.html", {
        'cliente': cliente,
        'cuentas': cuentas,
        'transacciones': transacciones,
        'ultimos_movimientos': ultimos_movimientos,
        'form': form
    })
