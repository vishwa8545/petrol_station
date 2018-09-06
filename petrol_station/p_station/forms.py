from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfileMode


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	type_station = forms.CharField(max_length=30)


	
		

