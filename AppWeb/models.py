from django.db import models

# Create your models here.

class Participante(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()

class Competencia(models.Model):
    #pass
    nombreCompetencia = models.CharField(max_length=60)

class Lugar(models.Model):
    #pass

    nombreLugar = models.CharField(max_length=60)

class Ejemplo(models.Model):

    nombreEjemplo = models.CharField(max_length=60)
