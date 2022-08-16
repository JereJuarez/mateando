from dataclasses import fields
import email
from xml.dom.minidom import parseString
from django import forms
from MatesApp import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    username= forms.CharField(label='Username (Nombre Matero)')
    email= forms.EmailField()
    password1= forms.CharField(label='Password (Contraseña)', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name= forms.CharField(label='Nombre')
    first_name= forms.CharField(label='Apellido')
    

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")


#PARA EL CHAT

class FormMensajes(forms.Form):
    mensaje= forms.CharField(widget=forms.Textarea(attrs= {

            "class": "formulario_ms",
            "placeholder": "Escribe tu mensaje"
    }))

    

#BLOG

class SendPostForm(forms.Form):                    

    nombre= forms.CharField(label='Nombre')
    contenido= forms.CharField(label="Contenido")
    imagen= forms.URLField(label='Link URL(imagen)')
    author= forms.CharField(label='Author')
