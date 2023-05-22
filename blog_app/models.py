from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha=models.DateTimeField(default=timezone.now)
    SECCION_CHOICES = (("Policiales", "Policiales"),("Deportes", "Deportes"),("Politica", "Politica"),("Interes General", "Interes General"),)
    seccion = models.CharField(max_length=1028, choices=SECCION_CHOICES)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)


    def __str__(self): 
       return f"Imagen de: {self.articulo}"