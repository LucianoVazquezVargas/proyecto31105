from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def curso(request):
    curso=Curso(nombre="Python",comision=31105)
    curso.save()
    texto=f"Curso creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

