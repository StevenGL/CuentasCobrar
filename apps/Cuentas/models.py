from django.db import models

# Create your models here.
class Estado(models.Model):
    Tipo = models.CharField(max_length = 8)
    
    def __str__(self):
            return self.Tipo
class Tipos_Movimientos(models.Model):
    Tipo = models.CharField(max_length = 2)
    
    def __str__(self):
            return self.Tipo

class Clientes(models.Model):
    Nombre =  models.CharField(max_length=50)
    Cedula =  models.CharField(max_length=11)
    Limite_Credito = models.DecimalField(max_digits=8, decimal_places = 2)
    Estado = models.ForeignKey(Estado, on_delete =models.CASCADE)
    
    def __str__(self):
            return self.Nombre

class Tipos_Documentos(models.Model):
    Descripcion = models.CharField(max_length=2000)
    Cuenta_Contable = models.PositiveIntegerField()
    Estado = models.ForeignKey(Estado, on_delete =models.CASCADE)

    def __str__(self):
        return self.Descripcion

class Transacciones(models.Model):
    Descripcion = models.CharField(max_length=2000)
    TipoDocumento = models.ForeignKey(Tipos_Documentos, on_delete = models.CASCADE)
    Tipo_Movimiento = models.ForeignKey(Tipos_Movimientos, on_delete = models.CASCADE)
    Numero_Documento = models.PositiveIntegerField()
    Fecha = models.DateField()
    Monto = models.DecimalField(max_digits=8, decimal_places = 2)
    Cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)

class Asientos_Contables(models.Model):
    Descripcion = models.CharField(max_length=2000)
    Cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    Tipo_Movimiento = models.ForeignKey(Tipos_Movimientos, on_delete = models.CASCADE)
    Cuenta = models.PositiveIntegerField()
    Fecha = models.DateField()
    Monto = models.DecimalField(max_digits=8, decimal_places = 2,)
    Estado = models.ForeignKey(Estado, on_delete =models.CASCADE) 
    
    