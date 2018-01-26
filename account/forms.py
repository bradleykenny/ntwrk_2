from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), required=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')