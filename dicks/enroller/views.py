from django.shortcuts import render
from django.views import generic
# Create your views here.
class SearchView(generic.DetailView)
    template_name = 'base.html'