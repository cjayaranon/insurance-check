from django.views import generic
from django.shortcuts import render
from enroller.models import PaymentTagging
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
