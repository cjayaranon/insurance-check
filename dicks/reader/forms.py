from django import forms
from django.utils import dateformat, formats


class ReportGenerateForm(forms.Form):
    
    from_date = forms.DateField(
        # input_formats = ['%Y/%m/%d'],
        widget = forms.DateInput(
            attrs = {
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
    to_date = forms.DateField(
        # input_formats = ['%d/%m/%Y'],
        widget = forms.DateInput(
            attrs = {
                'class': 'form-control',
                'type': 'date'
            }
        )
    )