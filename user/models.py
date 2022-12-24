import os

from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def image_location(instance, filename):
    file_path = 'profile/user_{username}/profile.jpeg'.format(
        username=str(instance.id), filename=filename,
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, code, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have their first_name")
        if not password:
            raise ValueError("Must secure account with password")
        if not code:
            raise ValueError("user must have a coupon code")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            code=code,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, code, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            code=code,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code = models.CharField(max_length=12, unique=True, blank=False)
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
        return reverse('user:profile', args=[self.username])

    def get_referral_link(self):
        return reverse('user:custom_account_signup', args=[self.code])

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserReferralLink(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    refered_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="refered_user")
        
    def __str__(self):
        return f"{self.refered_user} refered by {self.user}"


"""
# signals
"""

@receiver(post_save, sender=CustomUser)
def save_profile_img(sender, instance, *args, **kwargs):
    
    SIZE = 600, 600
    if instance.picture:
        pic = Image.open(instance.picture.path)
        try:
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(instance.picture.path)
        except:
            if pic.mode in ("RGBA", 'P'):
                profile_pic = pic.convert("RGB")
                profile_pic.thumbnail(SIZE, Image.LANCZOS)
                profile_pic.save(instance.picture.path)

    if instance.referred_by:
        user= CustomUser.objects.get(username=instance.referred_by)
        UserReferralLink.objects.get_or_create(user=user, refered_user=instance)