from django.contrib import admin
from .models import GenerateCode, UsersBalance, DailyLoginTask, Withdraw, TaskPost, AdvertPost

# Register your models here.
class GenerateCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'generated_by', 'coupon_code']
    list_filter = ['generated_by', 'user']
    search_fields = []
    
class UsersBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'currency', 'affilate', 'task']
    list_filter = ['user']
    
    
class DailyLoginTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task_completed']
    list_filter = ['task_completed']
    

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_completed']
    list_filter = ['transaction_completed']
    
    
class TaskPostAdmin(admin.ModelAdmin):
    list_display = ['post_link', 'task_completed']
    list_filter = ['task_completed']
    
class AdvertPostAdmin(admin.ModelAdmin):
    list_display = ['post_link', 'task_completed']
    list_filter = ['task_completed']
    

admin.site.register(UsersBalance, UsersBalanceAdmin)
admin.site.register(GenerateCode, GenerateCodeAdmin)
admin.site.register(DailyLoginTask, DailyLoginTaskAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(TaskPost, TaskPostAdmin)
admin.site.register(AdvertPost, AdvertPostAdmin)