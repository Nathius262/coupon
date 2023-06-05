from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import CustomUser, UserReferralLink
from user.utils import generate_ref_code
from .models import GenerateCode, UsersBalance, Currency
from django.http.response import JsonResponse
from .constants import currency as c

# Create your views here.
def currency(request):
    context = {}
    if request.user.is_authenticated:
        currencies = Currency.values
        #print(currency)
        context = {
            "currency" :currencies,
            "user_currency": request.user.user_currency.currency
        }
    return context

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
        render_template = render(request, 'pipay/landing_page.html', {'loc': True,})
    return render_template

def couponVendor_view(request):
    context = {
        'user': CustomUser.objects.all().filter(is_staff=True),
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
    context['loc'] = True
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
    return render(request, "pipay/withdraw.html")