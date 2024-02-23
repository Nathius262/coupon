from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('coupon/vendors', couponVendor_view, name='coupon_vendor'),
    path('coupon/generate', generateCoupon_view, name='generate_code'),
    path('coupon/verify', couponVerify_view, name='coupon_verify'),
    path('withdraw/', withdraw_view, name='withdraw'),
    path('withdraw/list/', withdraw_list_view, name='withdraw_list'),
    path('currency/change/', changeCurrency_view, name='currency_change'),
    path('user/currency/info/', userBalanceInfo, name='user_balance_info'),
    path('task/post/', task_post_view, name='task_post'),
    path('advert/post/', advert_post_view, name='advert_post'),
    path('paygig/', pay_gig_view, name='pay_gig'),
    path('top_earners/', topEarners_view, name='top_earners'),
]