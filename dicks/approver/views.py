from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
# from django.urls import reverse
from enroller.models import PaymentDetails

# Create your views here.



class BMapprove(generic.TemplateView):
    model = PaymentDetails
    template_name = 'update/pay-approval.html'
    
    def get(self, request, *args, **kwargs):
        client_list = PaymentDetails.objects.all()
        
        return render(request, self.template_name, {'query_list':client_list})
        
        
        
class ApproveView(generic.TemplateView):
    # model = PaymentDetails
    template_name = 'update/paymentdetails_update_form.html'
    success_url = 'pay-approver-link'
    
    def get(self, request, *args, **kwargs):
        info_list = PaymentDetails.objects.filter(id=kwargs['pk']).values_list(
            'payor',
            'encoder_branch',
            'membership_branch',
            'date_of_payment',
            'recording_date',
            'update_date',
            'cutoff_period',
            'premium_paid',
            'auth_agent',
            'payment_type',
            'tagging',
            'beneficiary1',
            'beneficiary2',
        )
        label_list = [
            'Payor',
            'Encoder Branch',
            'Membership Branch',
            'Date of Payment',
            'Recording Date',
            'Payment Last Updated',
            'Cut-off Period',
            'Premium Paid',
            'Agent',
            'Payment Type',
            'Tagging',
            'Beneficiary 1',
            'Beneficiary 2'
            ]
        
        final_list = []
        for items in info_list:
            for v in items:
                final_list.append(v)
                
        full_list = zip(label_list, final_list)
        print(full_list)
        return render(request, self.template_name, {'full_list':full_list})
        
        