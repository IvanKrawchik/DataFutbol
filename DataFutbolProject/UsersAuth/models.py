from django.db import models
from django.conf import settings

# Create your models here.
class Equipos(models.Model):
    equipo_id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Jugadores(models.Model):
    jugador_id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=3)
    edad = models.DateField()
    altura = models.CharField(max_length=5)
    nacionalidad = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipos,null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre, self.posicion, self.equipo_id

class Tecnicos(models.Model):
    tecnico_id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.DateField()
    equipo = models.ForeignKey(Equipos,null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre, self.equipo_id