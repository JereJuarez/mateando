import email
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
import uuid
from django.db.models import Count

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


#------------------------------------
#--------------md-------------------#
#------------------------------------

User= settings.AUTH_USER_MODEL

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    tiempo= models.DateTimeField(auto_now_add=True)
    actualizar= models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True


class CanalMensaje(ModelBase):
    canal= models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    texto= models.TextField()


class CanalUsuario(ModelBase):
    canal= models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)


class CanalQuerySet(models.QuerySet):

    def solo_uno(self):
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

    def solo_dos(self):
        return self.annotate(num_usuarios= Count("Usuarios").filter(num_usuarios=2))



class CanalManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)
    

class Canal(ModelBase):

    usuarios= models.ManyToManyField(User, blank=True, through=CanalUsuario)


    objects= CanalManager()
   