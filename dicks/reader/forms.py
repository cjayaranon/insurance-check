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