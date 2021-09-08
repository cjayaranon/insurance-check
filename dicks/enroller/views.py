from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from formtools.preview import FormPreview
# from .preview import BioEncodeFormPreview
from .models import *
from .forms import *

# Create your views here.



class SearchMixin(object):
    def dispatch(self, request, *args, **kwargs):
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
        return super().dispatch(request, *args, **kwargs)



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
    

    
class SearchView(generic.TemplateView):
    template_name = 'create/search.html'
    
    def get(self, request, *args, **kwargs):
        query = kwargs['string']
        
        query_list = Client.objects.filter(
            last_name__contains=query
            ) | Client.objects.filter(
            first_name__contains=query
            ) | Client.objects.filter(
            middle_name__contains=query
            ) | Client.objects.filter(
            iaccs_id__contains=query)
            
        return render(request, self.template_name, {'query_list':query_list, 'searchtext':query})
    
    
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
            
        return render(request, self.template_name, {'query_list':query_list, 'searchtext':query})


        
class BioEncodeView(generic.CreateView):
    form_class = BioEncodeForm
    template_name = 'create/bio-encode.html'
    # add code for search bar
        
        
        
class BioEncodeFormPreview(FormPreview):
    '''
    preview of bio-data encoding form
    '''
    
    def done(self, request, cleaned_data):
        data = Client(**cleaned_data)
        data.save()
        return HttpResponseRedirect(reverse('home'))
        
        
        
class PaymentEncodeView(generic.CreateView):
    '''
    accepts model.id from search results on views
    GET shows form with pre-selected Client in payor, membership_branch
    '''
    form_class = PaymentDetailsForm
    
    def get(self, request, *args, **kwargs):
        # set locked fields [payor, membership_branch, encoder_branch]
        # encoder_branch will be locked after login_required is enabled
        print('<----nag encode---->')
        template_name = 'create/payment-encode-details.html'
        client = Client.objects.get(id=kwargs['int'])
        
        form_class = PaymentDetailsForm(
            request.GET or None, initial={
                'payor':client.id,
                'membership_branch':client.membership_branch
                }
            )
        
        return render(request, template_name, {'form':form_class})
    
    
    def post(self, request, *args, **kwargs):
        '''
        used for the search bar on top of the page
        '''
        template_name = 'create/payment-encode-details.html'
        print('<----submitted payment form---->')
        if'searchtext' in request.POST:
            print('<----nag search---->')
            url = reverse('search', args=(request.POST['searchtext']))
            return HttpResponseRedirect(url)
        else:
            url = reverse('pay-preview')
            return HttpResponseRedirect(url)
        
        
        
class PaymentDetailsFormPreview(FormPreview):
    
    def done(self, request, cleaned_data):
        data = PaymentDetails(**cleaned_data)
        data.save()
        return HttpResponseRedirect(reverse('home'))
