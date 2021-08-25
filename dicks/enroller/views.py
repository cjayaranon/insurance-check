from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.
class SearchView(generic.DetailView):
    model = Client
    template_name = 'create/search.html'
    
    
    
class EncodeView(generic.CreateView):
    model = Client
    template_name = 'create/encode.html'
    fields = ['first_name','last_name']