from django.shortcuts import render
from django.utils import timezone
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def post_list(request):
	return render(request, 'charmi/post_list.html', {})

def profile_new(request):
	form = ProfileForm()
	return render(request, 'charmi/profile_edit.html', {'form': form})