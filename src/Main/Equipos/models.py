from django.db import models


class Integrantes(models.Model):
    Nombre = models.CharField(blank=False, max_length=120)
    Email = models.EmailField()

    def __str__(self):
        self.Nombre


class Equipos(models.Model):
    Nombre = models.CharField(blank=False, max_length=120)
    Integrador = models.ManyToManyField(Integrantes, through='Membresia')

    def __str__(self):
        return self.Nombre

class Membresia(models.Model):
    Integrantes = models.ForeignKey(Integrantes)
    Equipos = models.ForeignKey(Equipos)
    FechaRegistro = models.DateField(auto_now_add=True,auto_now=False)
    DescripcionInvitacion = models.CharField(max_length=100)

    def __str__(self):
        return self.FechaRegistro
