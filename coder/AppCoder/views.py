from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def curso(request):
    curso=Curso(nombre="Python",comision=31105)
    curso.save()
    texto=f"Curso creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")
