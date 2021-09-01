from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from formtools.preview import FormPreview
# from .preview import BioEncodeFormPreview
from .models import *
from .forms import *

# Create your views here.
class SearchView(generic.DetailView):
    model = Client
    template_name = 'create/search.html'
    
    
    
class BioEncodeView(generic.CreateView):
    form_class = BioEncodeForm
    template_name = 'create/bio-encode.html'
    
    def form_valid(self, form):
        # validate and clean form data
        # send to BioEncodeFormPreview
        print('yay')
        
        print(form)
        # self.object = form.save()
        # self.request.session.save()
        return HttpResponseRedirect('/enroller/encode')
        
        
        
class BioEncodeFormPreview(FormPreview):
    def done(self, request, cleaned_data):
        # do something with cleaned_data, then redirect to a success page
        return HttpResponseRedirect('/enroller/encode')
        
        
        
class PaymentEncodeView(generic.CreateView):
    form_class = PaymentDetailsForm
    template_name = 'create/payment-details.html'
    
    def form_valid(self, form):
        print('<------- PaymentEcode-------->')
        return HttpResponseRedirect('/enroller/encode/')
        
        
        
# class ReviewDetailsView(FormPreview):
#     def done(self, request, cleaned_data):
#         # do something
#         return HttpResponseRedirect()
