from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login-usuario/', login_usuario, name='login-usuario'),
    path('redirect-user/', login_redirect_user, name='login-redirect-user'),
    path('registro/', registro, name='registro-user'),
    path('dashboard/', dashboard_cliente, name='dashboard-cliente'),
    path('transacciones-cliente/<int:pk>', transacciones_cliente, name='transacciones-cliente'),
    path('envioDinero/<int:pk>', envio_dinero, name='envio-dinero'),
    path('deposito/<int:pk>', deposito, name='deposito'),
    path('dashboard-admin/', dashboard_admin, name='dashboard-admin'),
    path('transacciones/', transacciones, name='transacciones'),
    path('lista-clientes/', lista_clientes, name='lista-clientes'),
    path('datos-cliente/<int:pk>', datos_cliente, name='datos-cliente'),

]