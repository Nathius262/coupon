from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('coupon/vendors', couponVendor_view, name='coupon_vendor'),
    path('coupon/generate', generateCoupon_view, name='generate_code'),
    path('coupon/verify', couponVerify_view, name='coupon_verify'),
    path('withdraw/', withdraw_view, name='withdraw'),
    path('currency/change/', changeCurrency_view, name='currency_change'),
    path('user/currency/info/', userBalanceInfo, name='user_balance_info'),
    path('task/', advert_post_view, name='advert_post'),
    path('top_earners/', topEarners_view, name='top_earners'),
]