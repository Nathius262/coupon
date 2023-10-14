import uuid
from django.conf import settings
import os


def image_location(instance, filename):
    file_path = 'profile/user_{username}/profile.jpeg'.format(
        username=str(instance.id), filename=filename,
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path


def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code