from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', profile_view, name='profile'),
    path('referral/<str:username>', referrals_view, name='referred_user'),
    path('<str:ref_code>/referral/', refer_link_view, name='custom_account_signup'),
]