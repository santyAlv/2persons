from django.db import models


class Producto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.TextField(max_length=25)
    Cantidad = models.IntegerField()
    Precio = models.FloatField()
    Descripcion = models.TextField()
    Categoria = models.CharField(max_length=80)
    fecha_ingreso = models.DateField()
