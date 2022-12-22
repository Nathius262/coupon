from django.shortcuts import render
from django.contrib import messages
from user.models import User

# Create your views here.
def index_view(request):
    # the keyword "loc" of the dictionary below is to check if we are rendering the index page
    return render(request, 'pipay/home.html', {'loc': True,})

def dashboard_view(request):
    return render(request, 'pipay/dashboard.html')

def task_view(request):
    return render(request, 'pipay/task.html')

def couponVendor_view(request):
    context = {
        'user': User.objects.all(),
    }
    return render(request, 'pipay/couponVendor.html', context)

def couponVerify_view(request):

    context = {}
    if request.POST:
        
        coupon_verify = request.POST['verifyCoupon']
        user = User.objects.all().filter(code=str(coupon_verify))

        try:
            if str(coupon_verify) == str(user.first().code):
                context['users'] = user
            else:
                messages.error(request, "User with this coupon does not exit!")
        except AttributeError:
            messages.error(request, "User with this coupon does not exit!")
    return render(request, 'pipay/couponVerify.html', context)
