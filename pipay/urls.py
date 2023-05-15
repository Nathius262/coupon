from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('coupon/vendors', couponVendor_view, name='coupon_vendor'),
    path('coupon/generate', generateCoupon_view, name='generate_code'),
    path('coupon/verify', couponVerify_view, name='coupon_verify'),
    path('withdraw/', withdraw_view, name='withdraw'),
]