from django.contrib import admin
from .models import WithdrawalEnable, SaveWithdrawData

# Register your models here.
class WithdrawEnableAdmin(admin.ModelAdmin):
    list_display = ['enable',]
    #list_editable = ['enable',]
    
class SaveWithdrawDataAdmin(admin.ModelAdmin):
    list_display = ['user']
    
    
admin.site.register(WithdrawalEnable, WithdrawEnableAdmin)
admin.site.register(SaveWithdrawData, SaveWithdrawDataAdmin)