from django.db import models

class Contactos(models.Model):
    Nombre = models.CharField(max_length=120)
    Telefono = models.IntegerField(max_length=20)
    Direccion = models.CharField(max_length=120)
    Estado = models.BooleanField()
    Descripcion = models.TextField()

    def __str__(self):
        return self.Nombre


class Categoria():
    Codigo = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=120)
    Pertenecientes = models.ManyToManyField(Contactos, trough='Categoria')

    def __str__(self):
        return self.Nombre


class Directorio(models.Model):
    Contactos = models.ForeignKey(Contactos)
    Categoria = models.ForeignKey(Categoria)
    Cantidad = models.IntegerField(max_length=10000)


    def __str__(self):
        return self.Cantidad
