from contextvars import copy_context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest 
from MatesApp.models import Yerba, Avatar, CanalMensaje, CanalUsuario, Canal, CanalManager, CanalQuerySet
from MatesApp.forms import UserRegisterForm, UserEditForm, AvatarForm, FormMensajes
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormMixin
from django.views.generic import View
from django.conf.urls import handler404 





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

def prox(request):
    return render(request, "MatesApp/prox.html" )


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

        if formulario.is_valid():
            avatarViejo= Avatar.objects.get(user=request.user)
            if(avatarViejo.imagen):
                avatarViejo.delete()
            avatar= Avatar (user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'MatesApp/inicio.html', {'usuario':request.user, 'mensaje':"AVATAR AGREGADO CORRECTAMENTE"})          
               

    else:
        formulario= AvatarForm()

    return render(request, 'MatesApp/agregarAvatar.html', {'formulario':formulario, 'usuario':request.user}) 


@login_required
def chat(request):
    return render(request, "MatesApp/chat.html")

 

class Inbox(View):
    def get(self, request):

        inbox= Canal.objects.filter(canalusuario__usuario__in=[request.user.id])

        context= {
            "inbox":inbox
        }
        
        return render(request, 'MatesApp/inbox.html', context)

class CanalFormMixin(FormMixin):
    form_class= FormMensajes
    #success_url= "./"
    

    def get_success_url(self):
        return self.request.path


        
    def post(self, request, *args, **kwargs):


        
        

        if not request.user.is_authenticated:
            raise PermissionDenied
        
        form= self.get_form()
        if form.is_valid():
            canal= self.get_object()
            usuario= self.request.user
            mensaje= form.cleaned_data.get("mensaje")
            canal_obj= CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)


            #if request.is_ajax():
            #    return JsonResponse({
            #        
            #        'mensaje':canal_obj.texto,
            #        'username':canal_obj.usuario.username
            #    }, status=201)
            
            
            return super().form_valid(form)

        else:

            #if request.is_ajax():
            #    return JsonResponse({"Error":form.errors}, status=400)

            return super().form_invalid(form)


class CanalDetailView(LoginRequiredMixin, CanalFormMixin, DetailView ):
    template_name= 'MatesApp/canal_detail.html'
    queryset= Canal.objects.all()

    def get_context_data(self, *args, **kwargs):
        context= super(). get_context_data(*args, **kwargs)

        obj= context['object']
        print(obj)

        #if self.request.user not in obj.usuarios.all():
        #   raise PermissionDenied

        context['si_canal_miembro']= self.request.user in obj.usuarios.all()

        return context
    
    #OCULTADO (la var queryset la definí antes)
    #def get_queryset(self):
    #    usuario=self.request.user
    #    username=usuario.username
    #
    #    qs= Canal.objects.all().filtrar_por_username(username)
    #    return qs

class DetailMs(LoginRequiredMixin,CanalFormMixin, DetailView):

    template_name= 'MatesApp/canal_detail.html'

    def get_object(self, *args, **kwargs):
        username= self.kwargs.get("username")
        mi_username= self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)


        if username == mi_username:
            mi_canal, _= Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)

            return mi_canal

        if canal == None:
            raise Http404

        return canal

def mensajes_privados(request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")
    
    mi_username= request.user.username

    canal, created= Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("si, fue creado")

        
   
    Usuarios_Canal = canal.canalusuario_set.all().values("usuario__username")
    print(Usuarios_Canal)
    mensaje_canal= canal.canalmensaje_set.all()
    print(mensaje_canal.values("texto"))

    return HttpResponse(f"Nuestro Id del Canal - {canal.id}")




# Create your views here.
