from django.urls import path
from MatesApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('yerbas/', views.yerbas, name="yerbas"),
    path('login/', views.login_request, name= 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='MatesApp/logout.html'), name= 'logout')
]