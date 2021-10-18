from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from enroller.models import PaymentDetails, PaymentTagging

# Create your views here.



class BMapprove(generic.TemplateView):
    model = PaymentDetails
    template_name = 'update/pay-approval.html'
    
    def get(self, request, *args, **kwargs):
        # modify to fetch only PaymentDetails tagged as pending thru PaymentTagging
        query_list = PaymentTagging.objects.filter(tag='PENDING')
        
        return render(request, self.template_name, {'query_list':query_list})
        
        
        
class ApproveView(generic.TemplateView):
    '''
    contains PaymentDetails
    redirect here from BM landing/payments views
    '''
    template_name = 'update/paymentdetails_update_form.html'
    success_url = 'pay-approver-home'
    
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
        items = PaymentDetails.objects.get(pk=kwargs['pay_details'])
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
            # edit tag to CANCEL in PaymentTagging then redirect to BM home with warning message
            model = PaymentTagging(pk=kwargs['pay_tag'], tag='CANCEL', approver=request.user.agent, payment=PaymentDetails.objects.get(pk=kwargs['pay_details']))
            model.save()
            messages.warning(request, 'Payment successfully cancelled.')
        else:
            # add tag approved to PaymentTagging then redirect to BM home with success message
            model = PaymentTagging(pk=kwargs['pay_tag'], tag='APPROVE', approver=request.user.agent, payment=PaymentDetails.objects.get(pk=kwargs['pay_details']))
            model.save()
            messages.success(request, 'Payment successfully approved.')
        
        return HttpResponseRedirect(reverse('pay-approver-home'))
        
        