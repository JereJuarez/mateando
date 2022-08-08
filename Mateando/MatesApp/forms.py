from dataclasses import fields
import email
from xml.dom.minidom import parseString
from django import forms
from MatesApp import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email= forms.EmailField()
    contraseña1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    contraseña2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

        

    