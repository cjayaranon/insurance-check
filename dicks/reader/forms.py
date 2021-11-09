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
    
    
    
class OverallReportGenerateForm(forms.Form):
    CHOICES =(
        ('OVERALL','Overall Sales'),
        ('PREMIUM','By Premium Paid'),
        ('HO-ARD','HO/ARD')
    )
    report_format = forms.ChoiceField(
        choices = CHOICES,
        widget = forms.Select(
            attrs = {
                'class': 'form-control',
                'type':'button'
            }
        )
    )
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