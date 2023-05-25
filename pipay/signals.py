from django.db.models.signals import pre_save
from .models import UsersBalance
from .constants import Currency

def change_currency_signal(sender, instance, *args, **kwargs):
    try:
        new_user_data = instance
        old_user_data = UsersBalance.objects.get(user=instance.user)
        new_currency = str(new_user_data.currency)
        old_currency = str(old_user_data.currency)
        affilate = float(new_user_data.affilate)
        task = float(new_user_data.task)

        if(new_user_data.currency == old_user_data.currency):
            pass
        elif (old_currency != new_currency):
            # convert affilate earning to the new currency
            affilate = Currency().currencyConverter(old_currency, new_currency, affilate)
            # convert task earning to the new currency
            task = Currency().currencyConverter(old_currency, new_currency, task)
            # save new value for both task and affilate earnings
            instance.affilate = affilate
            instance.task = task
    except UsersBalance.DoesNotExist:
        pass
    
pre_save.connect(change_currency_signal, sender=UsersBalance)