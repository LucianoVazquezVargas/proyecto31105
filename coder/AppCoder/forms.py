from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision=forms.IntegerField()

class ProfeForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)   
    profesion=forms.CharField(max_length=50)
    email=forms.EmailField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)#El widget es para que muestre la password como asteriscos
    username= forms.CharField(label="Usuario")

    class Meta:#La clase Meta es una clase de configuracion del objeto donde esta metida
        model= User
        fields= ['username','email','password1','password2']
        #saco los textos de ayuda de eso
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model= User
        fields= ['email','password1','password2','first_name','last_name']
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")



