from django.contrib import admin
from .models import GenerateCode, UsersBalance, DailyLoginTask

# Register your models here.
class GenerateCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'coupon_code']
    list_filter = []
    search_fields = []
    
class UsersBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'currency', 'affilate', 'task']
    list_filter = ['user']
    
    
class DailyLoginTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task_completed']
    list_filter = ['task_completed']
    

admin.site.register(UsersBalance, UsersBalanceAdmin)
admin.site.register(GenerateCode, GenerateCodeAdmin)
admin.site.register(DailyLoginTask, DailyLoginTaskAdmin)