from django.shortcuts import render, HttpResponse
from .models import Cabains
# Create your views here.

# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def administrador(request):
    cabain = Cabains.objects.all()
    return render(request,'inicio/administrador.html',{'cabain':cabain})

def cabañas(request):
    return render(request,"inicio/cabañas.html")

def contacto(request):
    return render(request,"inicio/contacto.html")

def nosotros(request):
    return render(request,"inicio/nosotros.html")

def ayuda(request):
    return render(request,"inicio/ayuda.html")

