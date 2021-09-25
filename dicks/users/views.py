from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
# Create your views here.



class LoginScreen(generic.TemplateView):
    '''
    login screen for all users
    '''
    template_name = 'login.html'