from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import CustomUser, VendorProfile
from user.utils import generate_ref_code
from .models import GenerateCode, UsersBalance, Currency, DailyLoginTask, Withdraw, TaskPost, AdvertPost
from .forms import WithdrawalForm
from django.http.response import JsonResponse
from .constants import currency as c
from .utils import daily_task_process
from notifications.signals import notify
from decimal import Decimal


# Create your views here.
def currency(request):
    context = {}
    if request.user.is_authenticated:
        #check if daily login task is completed
        #if not completed do something...            
        try:
            user_dail_login_task = DailyLoginTask.objects.all().get(user=request.user, task_completed=False)
            if (user_dail_login_task) and (user_dail_login_task.task_completed ==False):
                user_dail_login_task.task_completed = True
                user_dail_login_task.save()
                #daily login bonus
                topup = 200
                daily_task_process(request.user, topup)
                notify.send(user_dail_login_task, recipient=request.user, verb="Daily login bonus", description=f"{topup} added to your task balance", level='success')
            else:
                pass
                
        except DailyLoginTask.DoesNotExist:
            pass
        
        currencies = Currency.values
        context = {
            "currency" :currencies,
            "user_currency": request.user.user_currency.currency
        }
    return context

# Create your views here.
def userBalanceInfo(request):
    context = {}
    if request.user.is_authenticated:
        
        user = request.user.user_currency
         
        context = {           
            "total_balance":user.totalBalance(),
            "total_earning": user.totalEarnings(),
            "total_withdraw": Decimal('0.00'), #user.totalWithdraw(),
            "affilate": user.affilate,
            "task": user.task,
            "currency": user.currency
        }
    return JsonResponse(context, safe=False)

def changeCurrency_view(request):
    
    if request.POST:
        get_user_currency = request.POST.get('currency')
        user = UsersBalance.objects.get(user=request.user)
        affliate = c.currencyConverter(user.currency, get_user_currency, float(user.affilate))
        task = c.currencyConverter(user.currency, get_user_currency, float(user.task))
        ### reasigning currency to the usersbalance model based on the currency they have chosen
        user.affilate = affliate
        user.task = task
        user.currency = get_user_currency
        user.save()        
        message = {
            "status": "currency changed"
        }
    return JsonResponse(message, safe=True)

def index_view(request):
    # the keyword "loc" of the dictionary below is to check if we are rendering the index page
    
    if request.user.is_authenticated:        
        try:
            user_balance = UsersBalance.objects.get(user=request.user)
        except UsersBalance.DoesNotExist:
            return None
        
        context={
            'loc': False,
            'user_balance': user_balance
        }
        
        render_template = render(request, 'pipay/dashboard.html', context)
    else:
        context = {
          'loc': True,
        }
        render_template = render(request, 'pipay/landing_page.html', context)
    return render_template

def couponVendor_view(request):
    context = {
        'user': VendorProfile.objects.all(),
        'loc':False,
    }
    return render(request, 'pipay/couponVendor.html', context)

def generateCoupon_view(request):
    context = {}
    if request.user.is_staff:
        if request.POST:
            code = generate_ref_code()
            # generating code and saving in the database "GenerateCode"
            coupon_code, created = GenerateCode.objects.get_or_create(coupon_code=code, generated_by=request.user)
            if created:
                context['code'] = code
                context['show_code'] = True
    else:
        redirect('home')
    context['loc'] = False
    return render(request, 'pipay/generate_code.html', context)

def couponVerify_view(request):

    context = {}
    if request.POST:
        
        coupon_verify = request.POST['verifyCoupon']
        user = CustomUser.objects.all().filter(code=str(coupon_verify))

        try:
            if str(coupon_verify) == str(user.first().code):
                context['users'] = user
            else:
                messages.error(request, "User with this coupon does not exit!")
        except AttributeError:
            messages.error(request, "User with this coupon does not exit!")
    return render(request, 'pipay/couponVerify.html', context)

def withdraw_view(request):
    
    if request.GET:
        Withdraw.objects.all
    if request.POST:
        form = WithdrawalForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            obj = form.save(commit=False)
            obj.user = request.user
            save_info = request.POST['save_info']
            if save_info == "on":
                obj.save_info = True
            else:
                obj.save_info =False
            obj.save()
            print(obj)
    return render(request, "pipay/withdraw.html")

def topEarners_view(request):
    
    return render(request, "pipay/top_earners.html")

def task_post_view(request):
    post_obj = TaskPost.objects
    if request.POST:
        
        obj = post_obj.get(id=request.POST['post_id'], task_completed=False)
        obj.users.add(request.user)
        topup = 300
        daily_task_process(request.user, topup)
        notify.send(obj, recipient=request.user, verb="Task post bonus", description=f"{topup} added to your task balance", level='info')
        
        message={
            "message":"success"
        }
        return JsonResponse(message, safe=False)
    context = {
        'post': post_obj.all().filter(task_completed=False)
    }
    
    return render(request, "pipay/task.html", context)

def advert_post_view(request):
    post_obj = AdvertPost.objects
    if request.POST:
        
        obj = post_obj.get(id=request.POST['post_id'], task_completed=False)
        obj.users.add(request.user)
        topup = 300
        daily_task_process(request.user, topup)
        notify.send(obj, recipient=request.user, verb="Advert post bonus", description=f"{topup} added to your task balance", level='info')
        
        message={
            "message":"success"
        }
        return JsonResponse(message, safe=False)
    context = {
        'post': post_obj.all().filter(task_completed=False)
    }
    
    return render(request, "pipay/advert.html", context)