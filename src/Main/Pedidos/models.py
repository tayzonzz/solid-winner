from django.db import models

class Pedido(models.Model):
    Estado = models.BooleanField(default=True)
    Mensaje = models.TextField(blank=False)

    def __str__(self):
        return self.Estado
