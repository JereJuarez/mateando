from django.shortcuts import render
from django.http import HttpResponse
from MatesApp.models import Yerba, Avatar
from MatesApp.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#URL

@login_required
def inicio(request):

    avatares= Avatar.objects.filter(user=request.user.id)

    return render(request, "MatesApp/inicio.html", {"url":avatares[0].imagen.url})

@login_required
def yerbas(request):
    
    avatares= Avatar.objects.filter(user=request.user.id)

    return render(request, "MatesApp/yerbas.html", {"url":avatares[0].imagen.url})

def __str__(self):
    return f"Nombre: {self.nombre} - Edad {self.edad} - Yerba {self.yerba}"

@login_required
def busquedaMarca(request):
    return render(request, "MatesApp/busquedaMarca.html")

@login_required
def busquedaTipo(request):
    return render(request, "MatesApp/busquedaTipo.html")

@login_required
def busquedaPeso(request):
    return render(request, "MatesApp/busquedaPeso.html")


#BUSQUEDA YERBAS


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




#LOGIN/REGISTER/LOGOUT/EDITARPERFIL


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



#agregar login_required
def editarPerfil(request):

    usuario= request.user

    if request.method =='POST':
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            usuario.email= informacion['email']
            usuario.password1= informacion['password2']
            usuario.passwor2= informacion['password1']
            usuario.save()

            return render(request, "MatesApp/inicio.html")
    
    else:

        miFormulario= UserEditForm(initial={'email':usuario.email})

    return render(request, "MatesApp/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})   

#para la cambia la foto

@login_required
def agregarAvatar(request):
    if request.method == 'POST':

        formulario= AvatarForm(request.POST, request.FILES)

        if formulario.is_valid:

            u= Avatar.objects.get(user=request.user)
            avatar= Avatar (user=u, imagen=formulario.cleaned_data['imagen'])
            avatar.save()            
            return render(request, "MatesApp/inicio.html")   

    else:
        formulario= AvatarForm()

    return render(request, "MatesApp/agregarAvatar.html", {"formulario":formulario}) 


@login_required
def chat(request):
    return render(request, "MatesApp/chat.html")




# Create your views here.
