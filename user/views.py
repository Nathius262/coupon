from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AccountSettingsForm
from django.contrib import messages

# Create your views here.
def account_setting_view(request):
    
    if request.POST:
        
        form = AccountSettingsForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "first_name": request.POST['first_name'],
                "last_name": request.POST['last_name'],
                "phone_number_0": request.POST['phone_number_0'],
                "phone_number_1": request.POST['phone_number_1'],
                "picture": request.user.picture
            }
            
            form.save()
        
    else:
        form = AccountSettingsForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "phone_number": request.user.phone_number,
                "picture": request.user.picture
            }
        )
        
    context = {
        'form': form,
    }
    return render(request, 'user/account.html', context)


def refer_link_view(request, *args, **kwargs):
    code = str(kwargs.get('username'))
    print(code)
    try:
        user = CustomUser.objects.get(username=code)
        request.session['ref_user'] = user.id
        messages.info(request, f'you are about to sign up with "{user}" as a referral')
    except:
        pass
    #print(request.session.get_expiry_date())
    return redirect('account_signup')

def referral_list_view(request, *args, **kwargs):
    context={
        'referral_list':ReferralList.objects.get(user=request.user),
        'loc':False
    }
    return render(request, "user/referral_list.html", context)

def vendor_profile_view(request):
    if request.POST:
        user = CustomUser.objects.get(username=request.POST['user'])
        whatsapp_link = request.POST['whatsapp_link']
        bank_name = request.POST['bank_name']
        obj, created = VendorProfile.objects.get_or_create(user=user, whatsapp_link=whatsapp_link, bank_name=bank_name)
        if created:
            user.is_staff = True
            user.save()
        messages.success(request, f'{request.user} has been added as a vendor')
        return redirect('/')
            
    return render(request, "user/vendor_profile.html")
        