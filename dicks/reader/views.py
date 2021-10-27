from .forms import *
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from enroller.models import PaymentTagging
from formtools.preview import FormPreview
# Create your views here.



class PendingPayments(generic.TemplateView):
    model = PaymentTagging
    template_name = 'read/payments-view.html'
    call_name = 'pending-payments'
    
    
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(tag='PENDING')
        return render(request, self.template_name, {'query_list':query_list, 'call_name':self.call_name})
        
        
        
class ApprovedPayments(generic.TemplateView):
    model = PaymentTagging
    template_name = 'read/payments-view.html'
    call_name = 'approved-payments'
    
    
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(tag='APPROVE')
        return render(request, self.template_name, {'query_list':query_list, 'call_name':self.call_name})
        
        
        
class CancelledPayments(generic.TemplateView):
    model = PaymentTagging
    template_name = 'read/payments-view.html'
    call_name = 'cancelled-payments'
    
    
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(tag='CANCEL')
        return render(request, self.template_name, {'query_list':query_list, 'call_name':self.call_name})
        
        
        
class OwnBranchSales(generic.FormView):
    # model = PaymentTagging
    template_name = 'read/own-sales-home.html'
    form_class = ReportGenerateForm
    success_url = '/approver/'
    
    
class OwnBranchSalesFormPreview(FormPreview):
    '''
    preview of from_date and to_date
    '''
    
    def done(self, request, cleaned_data):
        # data = **cleaned_data
        print(cleaned_data)
        
        # change to results viewing
        return HttpResponseRedirect(reverse('pay-approver-home'))
        
        
        
class OwnBranchSalesResultsView(generic.TemplateView):
    template_name = 'read/sales-view.html'
