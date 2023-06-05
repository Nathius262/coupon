from django.db import models
from user.models import CustomUser


# Create your models here.
class GenerateCode(models.Model):
    coupon_code = models.CharField(max_length=12, unique=True)
    generated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=False, related_name="generated_by")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="user_code")

    def __str__(self):
        return str(self.coupon_code)

class Currency(models.TextChoices):
    dollar = '$'
    usd = 'USD'
    naira= 'N'
    pakistani_rupee= 'PKR'
    indian_rupee = 'INR'
    ghanaian_cedis= 'GHS'
    phillippine_peso = 'PHP'
    south_african_rand = "ZAR"
    
    
    def __str__(self):
        return str(self.id)
    
class UsersBalance(models.Model):
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_currency_valid",
                check=models.Q(currency__in=Currency.values)
            )
        ]
    
    user = models.OneToOneField(CustomUser, null=False, blank=False, on_delete=models.CASCADE, editable=False, related_name="user_currency")
    currency =models.CharField(max_length=50, editable=False, choices=Currency.choices, default=Currency.naira)
    affilate = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, editable=False)
    task = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, editable=False)
    
    def totalBalance(self):
        total_balance = self.affilate + self.task
        return total_balance
    
    def totalWithdraw(self):
        total_withdraw = self.totalBalance
        return total_withdraw
    
    def __str__(self):
        return str(self.user)
    