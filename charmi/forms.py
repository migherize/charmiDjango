from django import forms
from django.contrib.auth.models import User
from .models import	 *
from django.contrib.auth.forms import UserCreationForm

class Register(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    firstname = forms.CharField(label='firstname', max_length=30)
    lastname = forms.CharField(label='lastname', max_length=30)
    email = forms.CharField(label='Correo', widget=forms.EmailInput(), max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=100)

class Login(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), max_length=100)

class Forget(forms.Form):
    email = forms.CharField(label='Correo', widget=forms.EmailInput(), max_length=100)

class Foto(forms.Form):
	modelo = Photo
	fields = ['ruta']