from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from enroller.models import PaymentDetails

# Create your views here.



class BMapprove(generic.TemplateView):
    model = PaymentDetails
    template_name = 'update/pay-approval.html'
    
    def get(self, request, *args, **kwargs):
        client_list = PaymentDetails.objects.all()
        
        return render(request, self.template_name, {'query_list':client_list})