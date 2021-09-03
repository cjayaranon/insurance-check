from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from formtools.preview import FormPreview
# from .preview import BioEncodeFormPreview
from .models import *
from .forms import *

# Create your views here.



class HomeView(generic.TemplateView):
    '''
    landing page after login
    contains search
    '''
    
    template_name = 'create/search.html'
    def post(self, request, *args, **kwargs):
        query = request.POST['searchtext']
        query_list = Client.objects.filter(
            last_name__contains=query
            ) | Client.objects.filter(
            first_name__contains=query
            ) | Client.objects.filter(
            middle_name__contains=query
            ) | Client.objects.filter(
            iaccs_id__contains=query)
            
        # request.session['results_list'] = query_list
        # return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'query_list':query_list, 'searchtext':query})
    
    
class SearchView(generic.DetailView):
    model = Client
    template_name = 'create/search.html'
    
    
class BioEncodeView(generic.CreateView):
    form_class = BioEncodeForm
    template_name = 'create/bio-encode.html'
        
        
        
class BioEncodeFormPreview(FormPreview):
    # preview_template = 'create/bio-encode-preview.html'
    def done(self, request, cleaned_data):
        # print('<----cleaned_data---->')
        # print(cleaned_data)
        data = Client(**cleaned_data)
        data.save()
        return HttpResponseRedirect(reverse('home'))
        
        
        
class PaymentEncodeView(generic.CreateView):
    form_class = PaymentDetailsForm
    template_name = 'create/payment-encode-details.html'
    
    def form_valid(self, form):
        print('<------- PaymentEcode-------->')
        return HttpResponseRedirect('/enroller/encode/')
        
        
        
# class ReviewDetailsView(FormPreview):
#     def done(self, request, cleaned_data):
#         # do something
#         return HttpResponseRedirect()
