from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('setting', account_setting_view, name='account_setting'),
    #path('referral/<str:username>', referrals_view, name='referred_user'),
    path('?id=<str:ref_code>', refer_link_view, name='custom_account_signup'),
]