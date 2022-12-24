from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.
def profile_view(request):
    return render(request, 'user/profile.html')

def referrals_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    ref_user = UserReferralLink.objects.all().filter(user=user)
    context = {
        'user':user,
        'ref_user': ref_user, 
    }
    return render(request, 'user/referred_users.html', context)

def refer_link_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        user = CustomUser.objects.get(code=code)
        request.session['ref_user'] = user.id
        messages.info(request, f'you are about to sign up with "{user}" as a referral')
    except:
        pass
    #print(request.session.get_expiry_date())
    return redirect('account_signup')