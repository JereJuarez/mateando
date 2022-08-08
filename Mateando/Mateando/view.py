from django.http import HttpResponse

def inicio(request):
    return HttpResponse("MATEANDOO")

def usuarios(request):
    
    return HttpResponse('vista usuarios')