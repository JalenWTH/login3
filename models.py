from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput

# Create your models here.

class MyUser(AbstractBaseUser):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	phone=models.CharField(max_length=13)
	email=models.EmailField(max_length=100,unique=True)
	password=models.CharField(max_length=100)
	USERNAME_FIELD='email'

class MyUser_Login(AuthenticationForm):
	class Meta:
		model=MyUser
		fields=['email', 'password']


class MyUser_Signup(ModelForm):
	class Meta:
		model=MyUser
		fields='__all__'
		labels={
		'fname':'First Name',
		'lname':'Last Name'
		}

		widgets={
		'phone':TextInput(attrs={
			'type':'tel',
			'placeholder':'123-456-7890'
			}),
		'email':TextInput(attrs={
			'placeholder':'example@gmail.com'
			})
		}

	