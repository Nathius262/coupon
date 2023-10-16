from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

#from django import http
#from django.contrib import messages
#from mptt.admin import DraggableMPTTAdmin, MPTTAdminForm


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'is_staff', 'is_active', 'email', 'username', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'referred_by', 'code', 'picture', 'date_joined', 'last_login')
    list_editable = ('is_staff',)

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff')
    search_fields= ('email', 'username')
    fieldsets = ()
    
    
class ReferralListAdmin(admin.ModelAdmin):
    list_display = ['user',]
    readonly_fields = ['user', 'user_list']
    
    
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'whatsapp_link', 'bank_name']
    readonly_fields = ['user', 'whatsapp_link', 'bank_name']


"""
class UserReferralAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "username"
    list_display = (
        'tree_actions', 'indented_title', 'related_products_count',
        'related_products_cumulative_count'
    )
    list_display_links = ('indented_title',)

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related product (for this specific UserReferralLink)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related product (in tree)'
    
    def _move_node(self, request):

        queryset = self.get_queryset(request)
        pasted_on = queryset.get(pk=request.POST.get('pasted_on'))

        if pasted_on.level == 2:
            self.message_user(
                request,
                message="Can't create 4th level referral_link",
                level=messages.ERROR,
            )
            return http.HttpResponse("Can't create 4th level referral_link")
        return super()._move_node(request)
"""
admin.site.register(CustomUser, AccountAdmin)
admin.site.register(ReferralList, ReferralListAdmin)
admin.site.register(VendorProfile, VendorProfileAdmin)
#admin.site.register(UserReferralLink, UserReferralAdmin)
