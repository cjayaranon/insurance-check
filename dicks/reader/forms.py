from django import forms


class ReportGenerateForm(forms.Form):
    from_date = forms.DateField(
        input_formats = ['%m/%d/%Y'],
        widget = forms.DateInput(
            attrs = {
                'class': ' form-control datetimepicker-input',
                'data-target': 'datepicker1'
            }
        )
    )
    to_date = forms.DateField(
        input_formats = ['%m/%d/%Y'],
        widget = forms.DateInput(
            attrs = {
                'class': ' form-control datetimepicker-input',
                'data-target': 'datepicker2'
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