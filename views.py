from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here

class HomeView(LoginRequiredMixin, View):
	template_name='login3/home.html'
	login_url = '../login'
	def get(self, request):
		return render(request, self.template_name, {})

class LoginView(LoginView):
	template_name='login3/login.html'
	authentication_form=MyUser_Login
	next_page='/home'

	def get(self, request):
		empty_form=self.authentication_form
		print(empty_form)
		return render(request, self.template_name, {'form':empty_form})

class SignupView(View):
	template_name='login3/signup.html'
	form_class=MyUser_Signup

	def get(self, request):
		empty_form=self.form_class
		return render(request, self.template_name, {'form':empty_form})

	def post(self, request, *args, **kwargs):
		filled_form=self.form_class(request.POST)
		if filled_form.is_valid():
			fname=filled_form.cleaned_data['fname']
			lname=filled_form.cleaned_data['lname']
			email=filled_form.cleaned_data['email']
			phone=filled_form.cleaned_data['phone']
			password=filled_form.cleaned_data['password']
			if MyUser.objects.filter(email__iexact=email).exists():
				#if a user is already registered with this email
				messages.add_message(request, messages.INFO,
				'An account has already been registered with this email address')
				info_messages=get_messages(request)
				return render(request, self.template_name, {'form':filled_form,'messages':info_messages})

			else:
				instance=MyUser(fname=fname,lname=lname,phone=phone,email=email,password=password)
				instance.save()
				return redirect('LoginView')

		else:
			messages.add_message(request, messages.INFO,
			'You entered invalid data.')
			info_messages=get_messages(request)
			filled_form=self.form_class(request.POST)
			return render(request, self.template_name, {'form':filled_form,'messages':info_messages})