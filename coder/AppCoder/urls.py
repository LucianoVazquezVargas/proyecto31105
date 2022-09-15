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
    path("leerProfesores/",leerProfesores,name="leerProfesores"),
    path("eliminarProfesor/<id>",eliminarProfesor,name="eliminarProfesor"),
    path("editarProfesor/<id>",editarProfesor,name="editarProfesor"),
    #cbv
    path("estudiante/list/",EstudianteList.as_view(),name="estudiante_listar"),
    path("estudiante/<pk>",EstudianteDetalle.as_view(),name="estudiante_detalle"),
    path("estudiante/nuevo/",EstudianteCreacion.as_view(),name="estudiante_creacion"),
    path("estudiante/editar/<pk>",EstudianteUpdate.as_view(),name="estudiante_editar"),
    path("estudiante/borrar/<pk>",EstudianteDelete.as_view(),name="estudiante_borrar"),

    #LOGIN REGISTER LOGOUT
    path ("login/",login_request,name="login"),
    path ("register/",register,name="register"),


]
