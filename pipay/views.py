from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import CustomUser, UserReferralLink
from user.utils import generate_ref_code
from .models import GenerateCode, UsersBalance

# Create your views here.
def index_view(request):
    # the keyword "loc" of the dictionary below is to check if we are rendering the index page
    if request.user.is_authenticated:
        """user = CustomUser.objects.all()
        context = {
            'loc': False,
            'members': user.count(),
            'referrals': UserReferralLink.objects.all().filter(user=request.user).count(),
        }
        """
        
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
            coupon_code, created = GenerateCode.objects.get_or_create(coupon_code=code)
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