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
    
    # def get_initial(self):
    #     initial = super(EditClientDetails, self).get_initial()
        # for visible in iter(self.fields):
        #     visible.field.widget.attrs['class'] = 'form-control'
    
    def post(self, request, *args, **kwargs):
        if 'searchtext' in request.POST:
            return HttpResponseRedirect('/enroller/search/%s' % request.POST['searchtext'])
        else:
            return super(EditClientDetails, self).post(request, **kwargs)
            
    def form_valid(self, form):
        # clean = form.cleaned_data
        # self.object = context.save(clean)
        return super(EditClientDetails, self).form_valid(form)
        
        
        
class EditPendingPayments(generic.UpdateView):
    # model = PaymentTagging
    model = PaymentDetails
    template_name = 'update/edit-pending-payment.html'
    fields = '__all__'
    
    def post(self, request, *args, **kwargs):
        call_name = 'edit-pending-payment'
        
        if 'searchtext' in request.POST:
            return HttpResponseRedirect('/enroller/search/%s' % request.POST['searchtext'])
        else:
            messages.success(request, 'Payment updated successfully')
            return super(EditClientDetails, self).post(request, **kwargs)
    