from django import forms

from .models import Employee, BankDetail


class BankDetailsForms(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = [
            'bank_id', 'bank_name', 'bank_ifsc'
        ]


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'age', 'address', 'city', 'state',
            'country', 'skill_sets'
        ]

