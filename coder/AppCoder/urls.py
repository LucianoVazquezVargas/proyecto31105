from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio,name="inicio"),
    path("cursos/",cursos,name="cursos"),
    path("estudiantes/",estudiantes,name="estudiantes"),
    path("profesores/",profesores,name="profesores"),
    path("entregables/",entregables,name="entregables"),
    path("busquedaComision/",busquedaComision,name="busquedaComision"),
    path("buscar/",buscar,name="buscar"),

]
