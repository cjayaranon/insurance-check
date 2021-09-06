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
        print(kwargs)
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
        
class BioEncodeView(generic.CreateView):
    form_class = BioEncodeForm
    template_name = 'create/bio-encode.html'
    # add code for search bar
        
        
        
class BioEncodeFormPreview(FormPreview):
    # preview_template = 'create/bio-encode-preview.html'
    def done(self, request, cleaned_data):
        # print('<----cleaned_data---->')
        # print(cleaned_data)
        data = Client(**cleaned_data)
        data.save()
        return HttpResponseRedirect(reverse('home'))
        
        
        
class PaymentEncodeView(generic.CreateView):
    
    def get(self, request, *args, **kwargs):
        # set locked fields [payor, membership_branch, encoder_branch]
        # encoder_branch will be locked after login_required is enabled
        
        form_class = PaymentDetailsForm(request.GET or None, initial={'payor':kwargs['int']})
        template_name = 'create/payment-encode-details.html'
        
        print(kwargs)
        return render(request, template_name, {'form':form_class})
    
    
    def post(self, request, *args, **kwargs):
        '''
        used for the search bar on top of the page
        '''
        if request.POST['searchtext']:
            print('<----nag search---->')
            url = reverse('search', args=(request.POST['searchtext']))
            raise Http404
        else:
            print('<----do nothing---->')
            return HttpResponseRedirect(reverse('pay-preview'))
    
    # def form_valid(self, form):
    #     print('<------- PaymentEcode-------->')
    #     return HttpResponseRedirect('/enroller/encode/')
        
        
        
class PayEncodeFormPreview(FormPreview):
    def done(self, request, *args, **kwargs):
        pass
