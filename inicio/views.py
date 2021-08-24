from django.shortcuts import render, HttpResponse, redirect
from .models import Cabains
from django.contrib import admin

# Create your views here.

# Create your views here.

def principal(request):
    cabain = Cabains.objects.all()
    count =False;
    return render(request,"inicio/principal.html",{'cabain':cabain,'count':count})

def administrador(request):
    cabain = Cabains.objects.all()
    return render(request,'inicio/administrador.html',{'cabain':cabain})

def cabañas(request,id):
    cabain = Cabains.objects.get(id=id)
    return render(request,"inicio/cabañas.html",{'cabain': cabain})

def contacto(request):
    return render(request,"inicio/contacto.html")

def nosotros(request):
    return render(request,"inicio/nosotros.html")

def ayuda(request):
    return render(request,"inicio/ayuda.html")


