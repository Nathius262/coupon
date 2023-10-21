from django import forms
from .models import Withdraw
from notifications.signals import notify

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = [
            'email', 'bank_name', 'first_name', 
            'last_name', 'account_balance', 'amount',
            ]