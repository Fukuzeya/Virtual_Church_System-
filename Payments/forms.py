from django import forms
import re
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date
from Management.models import Members
from .models import *


class TransactionForm(forms.ModelForm):
    payment_type = forms.Select()
    amount_paid = forms.DecimalField()
    transaction_number = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ['payment_type','amount_paid','transaction_number']

    def clean_amount_paid(self):
        amount = self.cleaned_data['amount_paid']
        if amount < 1:
            raise ValidationError('You can not perform a transaction with a negative value!')
        return amount

    # def clean_transaction_number(self):
    #     number = self.cleaned_data['transaction_number']
    #     contact_format = re.compile(r"^07\d{8}$")
    #     pattern = contact_format.search(number)
    #     if not pattern:
    #         raise ValidationError('Invalid phone number!')
    #     return number

    def __inti__(self):
        super().__init__(*args, **kwargs)
        self.fields['payment_type'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['amount_paid'].widget.attrs.update(
            {'class': 'form-control','Label':'Profile'})
        self.fields['transaction_number'].widget.attrs.update(
            {'class': 'form-control','Label':'Profile'})

 