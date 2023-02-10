from django.db import models

# Create your models here.
class GenerateCode(models.Model):
    coupon_code = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return str(self.coupon_code)