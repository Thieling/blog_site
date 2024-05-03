from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"Avatar for {self.user.username}"
    
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    contenido = models.TextField()
    imagen = models.URLField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=10)

    def __str__(self):
        return f"Articulo: {self.titulo} {self.contenido} {self.imagen} {self.fecha} {self.autor}"