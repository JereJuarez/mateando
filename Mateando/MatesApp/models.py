import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    yerba=models.CharField(max_length=40)

class Yerba(models.Model):

    marca=models.CharField(max_length=40)
    tipo=models.CharField(max_length=50)
    peso=models.IntegerField()



    



   