from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

### AbstractUser sirve para combinar la tabla user con la tabla cliente
class Cliente(AbstractUser):

    ### nombre, apellido, email y username se heredan de User
    rut = models.CharField(max_length=10, unique=True)
    direccion= models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)

    @property  ### si no es del staff se considera cliente
    def es_cliente(self):
        return not self.is_staff

    def __str__(self):
        return self.rut


class Cuenta(models.Model):    

    TIPO_CUENTA = [
            ('AHORRO', 'Cuenta ahorro'),
            ('CORRIENTE', 'Cuenta corriente'),
            ('VISTA', 'Cuenta vista')
        ]

    ESTADO_CUENTA = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva')
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, related_name='cliente_cuenta', null=True)
    numero_cuenta = models.CharField(max_length=12)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA, default='vista')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CUENTA, default='activa')

    def __str__(self):
        return f'{self.numero_cuenta}'


class Destinatario(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_destinatario')
    nombre = models.CharField(max_length=100, null=False, blank=False)
    rut = models.CharField(max_length=10, unique=True)
    email = models.EmailField(null=False)
    cuenta = models.CharField(max_length=12)
    banco = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Transaccion(models.Model):

    TIPO_TRANSACCION = [
            ('DEPOSITO', 'Deposito'),
            ('RETIRO', 'Retiro'),
            ('TRANSFERENCIA', 'Transferencia')
        ]

    cuenta = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, related_name='cuenta_transaccion', null=True)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPO_TRANSACCION)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.SET_NULL, related_name='destinatario', null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo_transaccion} de ${self.monto} a {self.destinatario.nombre}'




