from django.forms import ModelForm, DateInput
from .models import *


class DateInput(DateInput):
    input_type = 'date'



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
            
        # self.fields['date_of_payment'].widget.attrs = {
        #     'class': 'form-control datetime-input',
        # }
    class Meta:
        
        model = PaymentDetails
        fields = '__all__'
            # 'payor',
            # 'encoder_branch',
            # 'membership_branch',
            # 'date_of_payment',
            # 'premium_paid',
            # 'auth_agent',
            # 'payment_type',
            # 'tagging',
            # 'beneficiary1',
            # 'beneficiary2'
        # ]
        widgets = {
            'date_of_payment': DateInput()
        }