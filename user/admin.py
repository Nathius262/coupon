from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    list_editable = ('first_name', 'last_name')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)
