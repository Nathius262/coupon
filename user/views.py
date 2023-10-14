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
    code = str(kwargs.get('ref_code'))
    try:
        user = CustomUser.objects.get(code=code)
        request.session['ref_user'] = user.id
        messages.info(request, f'you are about to sign up with "{user}" as a referral')
    except:
        pass
    #print(request.session.get_expiry_date())
    return redirect('account_signup')