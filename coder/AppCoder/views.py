from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")


def entregables(request):
    return render(request,"AppCoder/entregables.html")

'''def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre,comision=comision)
        curso.save()


    return render(request,"AppCoder/cursoFormulario.html")
'''
#Esta de abajo es la que se usa de verdad
def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data#cleaned_data es un diccionario
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            return render (request,"AppCoder/inicio.html")
    else:
        formulario=CursoForm()
        return render (request,"AppCoder/cursos.html",{"formulario":formulario})


def profesores(request):
    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            profesion=info["profesion"]
            email=info["email"]
            profe=Profesor(nombre=nombre,apellido=apellido,profesion=profesion,email=email)
            profe.save()
            return render(request,"AppCoder/inicio.html")
    else:
        form=ProfeForm()
    return render(request,"AppCoder/profesores.html",{"formulario":form})
    
def busquedaComision(request):
    return render(request,"AppCoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:

        comision=request.GET["comision"]
     #Trae de la base TODOS los cursos con esa comision(existen all,filter y get)
        cursos=Curso.objects.filter(comision=comision)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request,"AppCoder/busquedaComision.html"),{"mensaje":"ingrese una comision"}






