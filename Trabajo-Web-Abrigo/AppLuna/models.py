
import email
from django.db import models

# Create your models here.


class Dueno(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    
    
    

class Perro(models.Model):

    nombre = models.CharField(max_length=60)
    raza = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60)
    edad = models.IntegerField()

class Gato(models.Model):

    nombre = models.CharField(max_length=60)
    raza = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60)
    edad = models.IntegerField()

class Roedor(models.Model):

    nombre = models.CharField(max_length=60)
    raza = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60)
    edad = models.IntegerField()
