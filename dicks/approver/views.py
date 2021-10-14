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
    '''
    contains PaymentDetails
    redirect here from BM landing/payments views
    '''
    template_name = 'update/paymentdetails_update_form.html'
    success_url = 'pay-approver-link'
    
    def get(self, request, *args, **kwargs):
        label_list = [
            'Payor',
            'Encoder Branch',
            'Membership Branch',
            'Date of Payment',
            'Recording Date',
            'Payment Last Updated',
            'Cut-off Period (YYYY-MM-DD)',
            'Premium Paid',
            'Agent',
            'Payment Type',
            'Tagging',
            'Beneficiary 1',
            'Beneficiary 2'
            ]
        # get paymentdetails, 1 returns 1 record only
        items = PaymentDetails.objects.get(pk=kwargs['pk'])
        info_list = [
            items.payor,
            items.encoder_branch,
            items.membership_branch,
            items.date_of_payment,
            items.recording_date,
            items.update_date,
            items.cutoff_period,
            items.premium_paid,
            items.auth_agent.user.first_name,
            items.payment_type,
            items.tagging,
            items.beneficiary1,
            items.beneficiary2,
        ]

        full_list = zip(label_list, info_list)
        
        return render(request, self.template_name, {'full_list':full_list})
        
        
    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            print('<----yay---->')
        else:
            print('<----yay again---->')
        
        