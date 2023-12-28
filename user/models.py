from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import MyAccountManager
from .utils import image_location


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=True, blank=True)
    code = models.CharField(max_length=12, unique=True, blank=False, null=True)
    referred_by = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to=image_location, default="default.jpg", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    login_status = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'code']

    objects = MyAccountManager()

    @property
    def picture_url(self):
        try:
            pic = self.picture.url
        except :
            pic = ''
        return pic

    @property
    def usersFullName(self):
        return f'{self.first_name} {self.last_name}'
        
    def get_absolute_url(self):
        return reverse('user:referred_user', args=[self.username])

    def get_referral_link(self):
        return reverse('user:custom_account_signup', args=[self.username])

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class ReferralList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=False, related_name="referral_user")
    user_list = models.ManyToManyField(CustomUser, related_name="referral_list")
    
    def __str__(self) :
        return str(self.user)
    
class VendorProfile(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=False, related_name="vendor_profile")
    whatsapp_link = models.URLField(max_length=200, db_index=True, unique=True, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    