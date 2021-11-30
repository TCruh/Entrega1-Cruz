from django.db import models

# Create your models here.

class Animal(models.Model):
    Raza = models.CharField(max_length=200)
    Nro_Patas = models.IntegerField()
    Dieta = models.CharField(max_length=10)
    

class Cientifico(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=30)
    Email = models.EmailField()
    Nacimiento = models.DateField()
    Especializacion = models.CharField(max_length=50)
    Es_Fotografo = models.BooleanField(default= 0)
    
class Aficionado(models.Model):
    Nombre = models.CharField(max_length=25)
    Email = models.EmailField()
    Nacimiento = models.DateField()
    Aficion = models.CharField(max_length=30)
    Es_Fotografo = models.BooleanField(default= 0)
    