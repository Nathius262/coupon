from .models import UsersBalance
from .constants import currency

def daily_task_process(user, top_up):
    print(f"{top_up} added to your task balance")
    task_balace = UsersBalance.objects.get(user=user.id)
    bonus_naira = top_up
    if currency.isBaseCurrency(task_balace.currency):
        task_balace.task += bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", task_balace.currency, bonus_naira)
        task_balace.task += bonus_naira
    task_balace.save()
    
    
def affilate_topup_process(referred_by, topup):
    print(f"{topup} added to your affilate balance")
    topup_balance = UsersBalance.objects.get(user=referred_by.id)
    bonus_naira = topup
    if currency.isBaseCurrency(topup_balance.currency):
        topup_balance.affilate += bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", topup_balance.currency, bonus_naira)
        topup_balance.affilate += bonus_naira
    topup_balance.save()