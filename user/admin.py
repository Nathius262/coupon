from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'is_staff', 'is_active', 'email', 'username', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    list_editable = ('is_staff',)

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff')
    fieldsets = ()


class UserReferralAdmin(admin.ModelAdmin):
    list_display = ['user', 'refered_user']
    list_filter = ['user', 'refered_user']
    search_fields = ['user', 'refered_user']

admin.site.register(CustomUser, AccountAdmin)
admin.site.register(UserReferralLink, UserReferralAdmin)
