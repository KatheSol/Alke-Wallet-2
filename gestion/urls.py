from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_cliente, name='login'),
    path('registro/', registro, name='registro-user'),
    path('dashboard/', dashboard_cliente, name='dashboard-cliente'),
    path('transacciones-cliente/', transacciones_cliente, name='transacciones-cliente'),
    path('envioDinero/', envio_dinero, name='envio-dinero'),
    path('deposito/', deposito, name='deposito'),
    path('dashboard-admin/', dashboard_admin, name='dashboard-admin'),
    path('transacciones/', transacciones, name='transacciones'),
    path('lista-clientes/', lista_clientes, name='lista-clientes'),
    path('datos-cliente/<int:pk>', datos_cliente, name='datos-cliente'),

]