from .models import UsersBalance
from .constants import currency
from user.models import CustomUser

def daily_task_process(user, top_up):
    task_balace = UsersBalance.objects.get(user=user.id)
    bonus_naira = top_up
    if currency.isBaseCurrency(task_balace.currency):
        task_balace.task += bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", task_balace.currency, bonus_naira)
        task_balace.task += bonus_naira
    task_balace.save()
    
    
def affilate_topup_process(referred_by, topup):

    topup_balance = UsersBalance.objects.get(user=referred_by.id)
    bonus_naira = topup
    if currency.isBaseCurrency(topup_balance.currency):
        topup_balance.affilate += bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", topup_balance.currency, bonus_naira)
        topup_balance.affilate += bonus_naira
    topup_balance.save()
    
def affilate_deduct_process(user, topup):
    topup_balance = UsersBalance.objects.get(user=user.user)
    bonus_naira = topup
    if currency.isBaseCurrency(topup_balance.currency):
        topup_balance.affilate -= bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", topup_balance.currency, bonus_naira)
        topup_balance.affilate -= bonus_naira
    topup_balance.save()
     
def task_deduct_process(user, top_up):
    task_balace = UsersBalance.objects.get(user=user.user)
    bonus_naira = top_up
    if currency.isBaseCurrency(task_balace.currency):
        task_balace.task -= bonus_naira
        
    else:
        bonus_naira = currency.currencyConverter("N", task_balace.currency, bonus_naira)
        task_balace.task -= bonus_naira
    task_balace.save()
    
# returns user's id if exit
def query_user_id(user):
    """returns the users instance

    Args:
        user (insance): username or instance object
    """
    try:
        return CustomUser.objects.get(username=user)
    except CustomUser.DoesNotExist:
        return None