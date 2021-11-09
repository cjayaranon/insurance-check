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
        query_list = self.model.objects.filter(
            tag='PENDING',
            payment__encoder_branch = request.user.agent.branch,
        )
        return render(request, self.template_name, {'query_list':query_list, 'call_name':self.call_name})
        
        
        
class ApprovedPayments(generic.TemplateView):
    model = PaymentTagging
    template_name = 'read/payments-view.html'
    call_name = 'approved-payments'
    
    
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(
            tag='APPROVE',
            payment__encoder_branch = request.user.agent.branch,
        )
        return render(request, self.template_name, {'query_list':query_list, 'call_name':self.call_name})
        
        
        
class CancelledPayments(generic.TemplateView):
    model = PaymentTagging
    template_name = 'read/payments-view.html'
    call_name = 'cancelled-payments'
    
    
    def get(self, request, *args, **kwargs):
        query_list = self.model.objects.filter(
            tag='CANCEL',
            payment__encoder_branch = request.user.agent.branch,
        )
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
        # GET user branch_name to filter encoder_branch sales only
        # GET records from db (go thru PaymentTagging to access PaymentDetails)
        query_list = PaymentTagging.objects.filter(
            tag = 'APPROVE',
            payment__encoder_branch = request.user.agent.branch,
            payment__date_of_payment__range = [cleaned_data['from_date'],
            cleaned_data['to_date']]).values_list('id', flat = True)
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
        result_list = []    # contains PaymentTagging objects
        all_sales = []  # contains all payments as int/str
        amounts_list = []   # contains list of unique payment values
        sales = []
        totals_list = dict()
        
        for items in query_list:
            query_object = PaymentTagging.objects.get(id=items)
            result_list.append(query_object)    
            all_sales.append(str(query_object.payment.premium_paid))
            amounts_list = set(all_sales)
            sales = {name:all_sales.count(name) for name in amounts_list}
            
        for items in sales:
        	totals_list[items] = float(items)*sales[items]

        total = sum(totals_list.values())
        
        browser_details = list((
            request.META['REMOTE_ADDR'],
            request.META['HTTP_HOST'],
            request.META['HTTP_SEC_CH_UA'],
            # request.META['OS']
            ))
        return render(request, self.template_name, {'result_list':result_list, 'total_sales':total, 'browser_details':browser_details})
        
        
        
class OverallBranchSales(generic.FormView):
    # model = PaymentTagging
    template_name = 'read/overall-sales-home.html'
    form_class = OverallReportGenerateForm
    success_url = '/approver/'



class OverallSalesFormPreview(FormPreview):
    '''
    preview of from_date and to_date
    GET PaymentDetails thru PaymentTagging based on choice in report_format
    '''
    
    def done(self, request, cleaned_data):
        # GET records from db (go thru PaymentTagging to access PaymentDetails)
        report_format = cleaned_data['report_format']
        query_list = []
        if report_format == 'OVERALL':
            query_list = PaymentTagging.objects.filter(
                tag = 'APPROVE',
                payment__date_of_payment__range = [cleaned_data['from_date'],
                cleaned_data['to_date']]).values_list('id', flat = True)
            # pass results to view
        elif report_format == 'PREMIUM':
            print('<----PREMIUM---->')
            pass
        elif report_format == 'HO-ARD':
            print('<----HO-ARD---->')
            pass
        else:
            print('<----NO SUCH FORMAT---->')
        date_range = list((str(cleaned_data['from_date']), str(cleaned_data['to_date'])))
        request.session['generated_report'] = list(query_list)
        request.session['date_range'] = date_range
        request.session['report_format'] = report_format
        # change to results viewing
        return HttpResponseRedirect(reverse('overall-sales-viewing'))
        
        
        
class OverallSalesResultsView(generic.TemplateView):
    '''
    Display of Sales Report in HO/ARD view
    '''
    template_name = 'read/sales-view.html'
    
    
    def get(self, request, *args, **kwargs):
        query_list = request.session.get('generated_report')
        result_list = []    # contains PaymentTagging objects
        all_sales = []  # contains all payments as int/str
        amounts_list = []   # contains list of unique payment values
        sales = []
        totals_list = dict()
        
        for items in query_list:
            query_object = PaymentTagging.objects.get(id=items)
            result_list.append(query_object)    
            all_sales.append(str(query_object.payment.premium_paid))
            amounts_list = set(all_sales)
            sales = {name:all_sales.count(name) for name in amounts_list}
            
        for items in sales:
        	totals_list[items] = float(items)*sales[items]

        total = sum(totals_list.values())
        
        browser_details = list((
            request.META['REMOTE_ADDR'],
            request.META['HTTP_HOST'],
            request.META['HTTP_SEC_CH_UA'],
            # request.META['OS']
            ))
        return render(request, self.template_name, {'result_list':result_list, 'total_sales':total, 'browser_details':browser_details})
        