from django import forms

from django.contrib.auth.models import User
from .models import	 Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('First_name','Last_name',)