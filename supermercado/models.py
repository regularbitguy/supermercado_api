from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre