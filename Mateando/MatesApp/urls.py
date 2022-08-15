from django.urls import path, re_path
from MatesApp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static




UUID_CANAL_REGEX= r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('yerbas/', views.yerbas, name="yerbas"),
    path('yerbas/busquedamarca/', views.busquedaMarca, name="busquedamarca"),
    path('yerbas/busquedatipo/', views.busquedaTipo, name="busquedatipo"),
    path('yerbas/busquedapeso/', views.busquedaPeso, name="busquedapeso"),
    path('buscar/', views.buscar),
    path('buscar2/', views.buscar2),
    path('buscar3/', views.buscar3),
    path('yerbas/prox/', views.prox, name="prox"),
    path('login/', views.login_request, name= 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='MatesApp/logout.html'), name= 'logout'),
    path('editarPerfil/', views.editarPerfil,name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="agregarAvatar"),
    path('chat/', views.chat, name='chat'),
    path('dm/<str:username>', views.mensajes_privados, name='cha-t'  ),
    path('ms/<str:username>', views.DetailMs.as_view(), name="detailms" ),
    re_path(UUID_CANAL_REGEX, views.CanalDetailView.as_view()),
    path('inbox/', views.Inbox.as_view(), name="inbox" ),
]