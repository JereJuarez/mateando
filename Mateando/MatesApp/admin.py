from django.contrib import admin
from .models import Avatar, Usuario, Yerba  
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Yerba)
admin.site.register(Avatar)