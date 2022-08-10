import email
from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    yerba=models.CharField(max_length=40)


class Yerba(models.Model):
    
    marca=models.CharField(max_length=40)
    tipo=models.CharField(max_length=50)
    peso=models.IntegerField()

    def __str__(self):
        return f"Marca: {self.marca} - Tipo: {self.tipo} - Peso: {self.peso}" 



class Avatar(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Usuario: {self.user}"


    



   