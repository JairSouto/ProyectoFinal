
from django.db import models

# Create your models here.
class Equipos(models.Model):
    nombre = models.CharField(max_length=30)
    
  

    seguidores = models.IntegerField()

    
class Asociados(models.Model):
    nombre = models.CharField(max_length=40)
    redes_sociales = models.CharField(max_length=30)

class Cursos(models.Model):
    nombre = models.CharField(max_length=70)
    jugadorpro = models.CharField(max_length=70)
    duracion = models.CharField(max_length=50)
    def __str__(self):
        return f'Nombre: {self.nombre} - JugadorPro: {self.jugadorpro} - Duracion:{self.duracion}'



  



