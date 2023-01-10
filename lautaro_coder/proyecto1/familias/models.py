from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    miembros = models.PositiveIntegerField()
    
class Miembro(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

class IngresoGasto(models.Model):
    fuente_ingreso = models.CharField(max_length=50)
    cantidad_ingresos = models.PositiveIntegerField()
    tipo_gasto = models.CharField(max_length=50)
    cantidad_gastos = models.PositiveIntegerField()
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)    