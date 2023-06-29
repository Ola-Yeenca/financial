from django import forms

class PersonalFinanceForm(forms.Form):
    CHOICES = (
        ('1', 'Compound Interest'),
        ('2', 'Loan Payment'),
        ('3', 'Investment Return'),
        ('4', 'Present Value'),
        ('5', 'Future Value'),
    )

    choice = forms.ChoiceField(choices=CHOICES)
    principal = forms.DecimalField()
    rate = forms.DecimalField()
    time = forms.DecimalField()
    future_value = forms.DecimalField(required=False)
    present_value = forms.DecimalField(required=False)
