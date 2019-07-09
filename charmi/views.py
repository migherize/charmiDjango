from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Profile
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView

# Create your views here.

def post_list(request):
	return render(request, 'charmi/post_list.html', {})

def profile_new(request):
	form = ProfileForm()
	return render(request, 'charmi/profile_edit.html', {'form': form})

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
            print(user)
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
                return HttpResponseRedirect('/main/')
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

