from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def send_email_view(instance):
    # Your view logic here
    obj = instance

    # Send email
    subject = 'Withdraw from Pipaytech.com'
    message = f'Hi {obj.user}! you have successfully withdraw {obj.user.user_currency.currency}{obj.amount} from your {obj.account_balance} balance.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [obj.user.email]

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

    # Optionally, you can handle success or failure
    return HttpResponse('Email sent successfully!')

def privacy_policy(request):
    return render(request, 'process/privacy_policy.html')