from django.db import models
from user.models import CustomUser

# Create your models here.
class WithdrawalEnable(models.Model):
    enable = models.BooleanField(default=False, null=True)
    

class SaveWithdrawData(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=False, on_delete=models.CASCADE, related_name="user_save_withdraw")
    email = models.EmailField(verbose_name="email", max_length=60, blank=False, null=True)
    bank_name = models.CharField(max_length=100, blank=False, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50, default="xxxxxx9309")