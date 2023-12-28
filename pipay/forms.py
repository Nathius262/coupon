from django import forms
from .models import Withdraw, CustomUser
from notifications.signals import notify

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = [
            'email', 'bank_name', 'first_name', 'save_info',
            'last_name', 'account_balance', 'amount', 'account_number',
            ]
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(WithdrawalForm, self).__init__(*args, **kwargs)


    def clean(self):
        super(WithdrawalForm, self).clean()

        amount = self.cleaned_data.get('amount')
        account_balance = self.cleaned_data.get('account_balance')
        user = self.request.user.user_currency

        if account_balance == 'affilate':
            if amount > user.affilate:
                self.errors['amount'] = self.error_class([f'only a maximum of {user.affilate} can be withdraw from your affilate balance'])
                
        elif account_balance == 'task':
            if amount > user.task:
                self.errors['amount'] = self.error_class([f'only a maximum of {user.task} can be withdraw from your task balance'])
                
        else:
            self.errors['amount'] = self.error_class([f'error validating amount'])
            
        
        return self.cleaned_data
