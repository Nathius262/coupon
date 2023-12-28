from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('setting', account_setting_view, name='account_setting'),
    path('referral/<str:username>', referral_list_view, name='referral_list'),
    path('user=<str:username>', refer_link_view, name='custom_account_signup'),
    path('vendor/create', vendor_profile_view, name="vendor_profile")
]