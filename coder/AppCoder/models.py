from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=50)#str,maximo 50
    comision=models.IntegerField()#int
    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.nombre+" "+str(self.apellido)
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+self.profesion
class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')
    def __str__(self):
        return self.user