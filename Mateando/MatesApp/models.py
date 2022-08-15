import email
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
import uuid
from django.db.models import Count
from django.apps import apps


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
        return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=2)

    def filtrar_por_username(self, username):
        return self.filter(canalusuario__usuario__username=username)


class CanalManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)
    
    def filtrar_ms_por_privado(self, username_a, username_b):
        return self.get_queryset().solo_dos().filtrar_por_username(username_a).filtrar_por_username(username_b)

    def obtener_o_crear_canal_usuario_actual(self, user):
        qs= self.get_queryset().solo_uno().filtrar_por_username(user.username)
        if qs.exists():
            return qs.order_by("tiempo").first, False

        canal_obj = Canal.objects.create()
        CanalUsuario.objects.create(usuario=user, canal=canal_obj)
        return canal_obj, True



    def obtener_o_crear_canal_ms(self, username_a, username_b):
        qs = self.filtrar_ms_por_privado(username_a, username_b)
        if qs.exists():
            
            return qs.order_by("tiempo").first(), False

        User=apps.get_model("auth", model_name='User')
        usaurio_a, usuario_b= None, None

        try:
            usuario_a= User.objects.get(username=username_a)
        except User.DoesNotExist:
            return None, False

        try:
            usuario_b= User.objects.get(username=username_b)
        except User.DoesNotExist:
            return None, False

        if usaurio_a== None or usuario_b == None:
            return None, False

        obj_canal= Canal.objects.create()
        User= apps.get_model("auth", model_name='User')
        canal_usuario_a= CanalUsuario(usuario=User.objects.get(username=username_a), canal=obj_canal)
        canal_usuario_b= CanalUsuario(usuario=User.objects.get(username=username_b), canal=obj_canal)
        CanalUsuario.objects.bulk_create([canal_usuario_a, canal_usuario_b])
        return obj_canal, True 


class Canal(ModelBase):

    usuarios= models.ManyToManyField(User, blank=True, through=CanalUsuario)


    objects= CanalManager()
   