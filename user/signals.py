"""
# signals
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import CustomUser

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