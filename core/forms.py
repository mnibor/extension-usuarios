from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		User = get_user_model()
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']