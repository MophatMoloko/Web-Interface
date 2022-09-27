from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import redirect_to_login


today = datetime.today()

#Creates a class to logout users out of the webinterface
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

#Creates a class to login users out of the webinterface
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

#Creates a class to redirect users to the home screen
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': today}

#Class to check if a user is authorized
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

#class RedirectToLoginView(redirect_to_login): 
 #   template_name = 'home/login.html'
