from django.db import models

class Rating(models.Model):
    Titulo = models.CharField(blank=False, max_length=100)
    Calificacion = models.IntegerField(blank=False, null=False, max_length=5)
    Estado = models.BooleanField(default=True)
    Comentario = models.TextField(blank=False)

    def __str__(self):
        return self.Comentario
