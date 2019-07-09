from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView

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

            user = User.objects.create_user(username, email, password,**extras)
            profile = Profile.objects.create(Sexo='M',User = user)
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
                return render(request, 'charmi/main.html', {'rankins': rankins})
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

