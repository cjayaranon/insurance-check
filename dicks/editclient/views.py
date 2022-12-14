from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from enroller.models import Client, PaymentTagging, PaymentDetails
from enroller.forms import BioEncodeForm

# Create your views here.



class EditClientDetails(generic.edit.UpdateView):
    model = Client
    # form_class = BioEncodeForm
    fields = '__all__'
    template_name = 'update/edit-client_update_form.html'
    success_url = '/enroller/'
    
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Client successfully edited')
        return super(EditClientDetails, self).post(request, **kwargs)
            
    def form_valid(self, form):
        return super(EditClientDetails, self).form_valid(form)
        
        
        
class EditPendingPayments(generic.UpdateView):
    model = PaymentDetails
    template_name = 'update/edit-pending-payment.html'
    fields = '__all__'
    success_url = '/enroller/'
    
    def post(self, request, *args, **kwargs):
        # call_name = 'edit-pending-payment'
        messages.success(request, 'Payment updated successfully')
        return super(EditPendingPayments, self).post(request, **kwargs)
        
        
    def form_valid(self, form):
        return super(EditPendingPayments, self).form_valid(form)
    