# Create your models here.
from django.contrib.auth.models import BaseUserManager


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