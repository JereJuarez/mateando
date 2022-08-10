from django.urls import path
from MatesApp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('yerbas/', views.yerbas, name="yerbas"),
    path('yerbas/busquedamarca/', views.busquedaMarca, name="busquedamarca"),
    path('yerbas/busquedatipo/', views.busquedaTipo, name="busquedatipo"),
    path('yerbas/busquedapeso/', views.busquedaPeso, name="busquedapeso"),
    path('buscar/', views.buscar),
    path('buscar2/', views.buscar2),
    path('buscar3/', views.buscar3),
    path('login/', views.login_request, name= 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='MatesApp/logout.html'), name= 'logout'),
    path('editarPerfil/', views.editarPerfil,name="EditarPerfil"),
    path('editarPerfil/agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('chat/', views.chat, name='chat'),
]