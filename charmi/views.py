from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView

from django.db import transaction


# Create your views here.

def post_list(request):
	return render(request, 'charmi/inicio.html', {})

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
            extras = {
                'first_name': form.cleaned_data['firstname'],
                'last_name': form.cleaned_data['lastname']
            }

            foto_basica = Photo.objects.create(ruta='../static/img/login.jpg')
            user = User.objects.create_user(username, email, password,**extras) 
            profile = Profile.objects.create(Sexo='M',User = user,Photo= foto_basica)

            direccion = Address.objects.create(Profile=profile)

            for g in Game_list.objects.iterator():
                Ranking.objects.create(Type='0',Cantidad='1000',Num_win='0',Num_lose='0',Num_draw='0',Game=g,Profile=profile) 

            return HttpResponseRedirect('/login/')

    else:
        form = Register()

    return render(request, 'charmi/register.html', {'form': form})


def signUp(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                rankins = user.profile.Rankings.all()
                direcciones = user.profile.Addresses.all()
                return render(request, 'charmi/main.html', {'rankins': rankins, 'direcciones':direcciones})
            else:
                return HttpResponseRedirect('/login/')
    else:
        form = Login()

    return render(request, 'charmi/login.html', {'form': form})


def signOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def forget(request):
    if request.method == 'POST':
        form = Forget(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            if user is not None:
                return HttpResponseRedirect('/register/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        form = Forget()
    return render(request, 'charmi/forget.html', {'form': form})
    

def main(request):
    return render(request, 'charmi/main.html', {})


def edit_perfil(request):
    user = request.user
    direcciones = user.profile.Addresses.all()
    return render(request, 'charmi/profile_edit.html', {'direcciones':direcciones})

def jugar_ajedrez(request):
    user = request.user
    rankins = user.profile.Rankings.first()
    direcciones = user.profile.Addresses.all()
    oponente = User.objects.get(username='charlesb')
    ran_oponente = oponente.profile.Rankings.first()
    dir_oponente = oponente.profile.Addresses.all()
    return render(request, 'charmi/Ajedrez.html', {'rankins': rankins, 'direcciones':direcciones, 'oponente':oponente,'ran_oponente':ran_oponente, 'dir_oponente':dir_oponente})


@transaction.non_atomic_requests
def victoria(request):
    user = request.user
    rankin = user.profile.Rankings.first()
    rankin.Cantidad += 10
    rankin.save()
    rankins = user.profile.Rankings.all()

    user2 = User.objects.get(username='charlesb')
    rankin2 = user2.profile.Rankings.first()
    rankin2.Cantidad -= 10 
    rankin2.save()
    rankins2 = user2.profile.Rankings.all()

    return render(request, 'charmi/main.html', {'rankins':rankins})

@transaction.non_atomic_requests
def derrota(request):
    user = request.user
    rankin = user.profile.Rankings.first()
    rankin.Cantidad -= 10
    rankin.save()
    rankins = user.profile.Rankings.all()

    user2 = User.objects.get(username='charlesb')
    rankin2 = user2.profile.Rankings.first()
    rankin2.Cantidad += 10 
    rankin2.save()
    rankins2 = user.profile.Rankings.all()

    return render(request, 'charmi/main.html', {'rankins':rankins})

@transaction.non_atomic_requests
def empate(request):
    user = request.user
    rankin = user.profile.Rankings.first()
    rankin.Cantidad -= 5
    rankin.save()
    rankins = user.profile.Rankings.all()

    user2 = User.objects.get(username='charlesb')
    rankin2 = user2.profile.Rankings.first()
    rankin2.Cantidad += 5
    rankin2.save()
    rankins2 = user.profile.Rankings.all()

    return render(request, 'charmi/main.html', {'rankins':rankins})