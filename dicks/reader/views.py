from .forms import *
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from enroller.models import PaymentTagging, PaymentDetails
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
        print(cleaned_data)
        # GET records from db (go thru PaymentTagging to access PaymentDetails)
        query_list = PaymentTagging.objects.filter(payment__date_of_payment__range = [cleaned_data['from_date'], cleaned_data['to_date']]).values_list('id', flat = True)
        # query_list = PaymentDetails.objects.filter(date_of_payment__range = [cleaned_data['from_date'], cleaned_data['to_date']])
        # pass results to view
        date_range = list((str(cleaned_data['from_date']), str(cleaned_data['to_date'])))
        request.session['generated_report'] = list(query_list)
        request.session['date_range'] = date_range
        # change to results viewing
        return HttpResponseRedirect(reverse('reports-viewing'))
        
        
        
class OwnBranchSalesResultsView(generic.TemplateView):
    template_name = 'read/sales-view.html'
    
    
    def get(self, request, *args, **kwargs):
        query_list = request.session.get('generated_report')
        result_list = []
        for items in query_list:
            result_list.append(PaymentTagging.objects.get(id=items))
        browser_details = list((
            request.META['REMOTE_ADDR'],
            request.META['HTTP_HOST'],
            request.META['HTTP_SEC_CH_UA'],
            request.META['OS']))
        print(request.session.get('date_range'))
        return render(request, self.template_name, {'result_list':result_list, 'browser_details':browser_details})
