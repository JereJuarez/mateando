from django.shortcuts import render
from django.http import HttpResponse
from MatesApp.models import Yerba
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

def busquedaMarca(request):
    return render(request, "MatesApp/busquedaMarca.html")

def busquedaTipo(request):
    return render(request, "MatesApp/busquedaTipo.html")

def busquedaPeso(request):
    return render(request, "MatesApp/busquedaPeso.html")



def buscar(request):
    if request.GET["marca"]:

        marca= request.GET["marca"]
        yerbas=Yerba.objects.filter(marca=marca)
        

        return render(request, "MatesApp/resultadosBusqueda.html", {"yerbas":yerbas, "marca":marca})

    else:
        
        return render(request, "MatesApp/error1.html")
         


    return HttpResponse(respuesta)
    
def buscar2(request):
    if request.GET["tipo"]:

        tipo= request.GET["tipo"]
        yerbas=Yerba.objects.filter(tipo=tipo)


        return render(request, "MatesApp/resultadosBusqueda.html", {"yerbas":yerbas, "tipo":tipo})

    else:
        
        return render(request, "MatesApp/error2.html")
         
         


    return HttpResponse(respuesta)

def buscar3(request):
    if request.GET["peso"]:

        peso= request.GET['peso']
        yerbas=Yerba.objects.filter(peso=peso)


        return render(request, "MatesApp/resultadosBusqueda.html", {"yerbas":yerbas, "peso":peso})

    else:

        return render(request, "MatesApp/error3.html")
        

        
         
         

    return HttpResponse(respuesta)







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
