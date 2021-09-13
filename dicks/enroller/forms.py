from django.forms import ModelForm
from .models import *



class BioEncodeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BioEncodeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        
        model = Client
        fields = [
            'iaccs_id',
            'membership_branch',
            'first_name',
            'middle_name',
            'last_name',
            'name_extension',
            'address',
            'gender',
            'civil_status',
            'birth_date',
            'email',
            'role'
        ]
        
        
        
class PaymentDetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaymentDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        
        model = PaymentDetails
        fields = [
            'payor',
            'encoder_branch',
            'membership_branch',
            'date_of_payment',
            'cutoff_period',
            'premium_paid',
            'auth_agent',
            'payment_type',
            'tagging',
            'beneficiary1',
            'beneficiary2'
        ]