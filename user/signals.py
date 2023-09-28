"""
# signals
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import CustomUser, ReferralList
from pipay.models import UsersBalance, DailyLoginTask
from pipay.utils import affilate_topup_process
#from pipay.utils import daily_task_process

@receiver(post_save, sender=CustomUser)
def create_users_profile(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        """
        user_balance_account creates a UsersBalance object related to the created user
        and topsup N4800/$10 to the new user
        
        user_daily_login_task_profile creates  a DailyLoginTAsk object as related to the created user
        """
        user_balance_account = UsersBalance(user=user, task=4800)
        user_balance_account.save()        
        
        user_daily_login_task_profile = DailyLoginTask(user=user)
        user_daily_login_task_profile.save()
        #create referral profile for new users
        ReferralList(user=user).save()
        

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