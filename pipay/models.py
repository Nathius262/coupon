from django.db import models
from user.models import CustomUser
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.
class GenerateCode(models.Model):
    """GenerateCode generates unique code for each users that is about to 
    register on this platform
    """
    coupon_code = models.CharField(max_length=12, unique=True, null=True, blank=False)
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
    """UsersBalance keeps the total balance of the user's task earning
    and affilate earnings which sums up to a total balance
    """
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_currency_valid",
                check=models.Q(currency__in=Currency.values)
            )
        ]
    
    user = models.OneToOneField(CustomUser, null=True, blank=False, on_delete=models.CASCADE, related_name="user_currency")
    currency =models.CharField(max_length=50, editable=False, choices=Currency.choices, default=Currency.naira)
    affilate = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    task = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    def totalBalance(self):
        total_balance = self.affilate
        return total_balance
    
    @property
    def totalWithdraw(self):
        total_withdraw = None
        return total_withdraw
    
    def totalEarnings(self):
        total_earnings = self.affilate + self.task
        return total_earnings
    
    def __str__(self):
        return str(self.user)


class DailyLoginTask(models.Model):
    
    """DailyLoginTask keeps a track of the users daily login bonus
    """
    user = models.OneToOneField(CustomUser, null=True, blank=False, on_delete=models.CASCADE, editable=False, related_name="user_daily_task")
    task_completed = models.BooleanField(default=False, null=True)


class Notification(models.Model):
    """
    Notification holds the records of most of the recent user earning
    
    """
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

class Withdraw(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=False, on_delete=models.CASCADE, related_name="user_withdraw")
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    bank_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=12, unique=True, blank=False, null=True)
    withdrawal_date = models.DateTimeField(verbose_name='date withdraw', auto_now_add=True)
    save_info = models.BooleanField(default=True)
    account_balance = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50, default="xxxxxx9309")
    amount = models.DecimalField(validators=[MinValueValidator(6000.00)], max_digits=12, decimal_places=2, default=6000.00)
    transaction_completed = models.BooleanField(default=False)
    
#class EarningHistory(models.Model):
#    user=models.ForeignKey()

class TaskPost(models.Model):
    post_link = models.URLField(blank=True)
    users = models.ManyToManyField(CustomUser, blank=True)
    task_completed = models.BooleanField(default=False)


class AdvertPost(models.Model):
    post_link = models.URLField(blank=True)
    users = models.ManyToManyField(CustomUser, blank=True)
    task_completed = models.BooleanField(default=False)
      