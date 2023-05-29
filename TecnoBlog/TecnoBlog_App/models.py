from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=64)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.titulo} | {self.autor} | {self.creador}"