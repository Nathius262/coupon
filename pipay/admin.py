from django.contrib import admin
from .models import GenerateCode

# Register your models here.
class GenerateCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'coupon_code']
    list_filter = []
    search_fields = []

admin.site.register(GenerateCode, GenerateCodeAdmin)