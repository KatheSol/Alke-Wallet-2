from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro-user'),
    path('dashboard/', dashboard_cliente, name='dashboard-cliente'),
    path('transacciones/', transacciones_cliente, name='transacciones-cliente'),
    path('envioDinero/', envio_dinero, name='envio-dinero'),
    path('deposito/', deposito, name='deposito'),

]