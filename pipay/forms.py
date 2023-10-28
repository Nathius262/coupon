from django import forms
from .models import Withdraw
from notifications.signals import notify

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = [
            'email', 'bank_name', 'first_name', 'save_info',
            'last_name', 'account_balance', 'amount', 'account_number',
            ]