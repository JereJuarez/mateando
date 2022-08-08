from django.shortcuts import render
from django.http import HttpResponse
from MatesApp.forms import UserRegisterForm
from MatesApp import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, "MatesApp/inicio.html")

def yerbas(request):
    return render(request, "MatesApp/yerbas.html")

def __str__(self):
    return f"Nombre: {self.nombre} - Edad {self.edad} - Yerba {self.yerba}"









def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            usuario= authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, 'MatesApp/inicio.html', {'form':form, 'mensaje': f"Calenta la pava {usuario}"})
            
            else:
                return render(request,'MatesApp/inicio.html', {'form':form, 'mensaje': f"Error, nombre o contraseña incorrecta"})

        else: 

                return render(request, "MatesApp/login.html", {'form':form, 'mensaje': f"Error, formulario erroneo"})
    else:
        form = AuthenticationForm()
        return render(request,"MatesApp/login.html", {'form':form})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,'MatesApp/inicio.html', {'mensaje':f"Matero Creado: {username}"})
    

    else:
        form= UserRegisterForm()

    return render(request,'MatesApp/registro.html', {'form':form})





# Create your views here.
