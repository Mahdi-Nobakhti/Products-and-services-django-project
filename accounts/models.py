from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
import os

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user',default='default.jpg')

    def __str__(self) -> str:
        return self.username

@receiver(pre_delete, sender=CustomUser)
def delete_product_images(sender, instance, **kwargs):
    # حذف تصویر مرتبط با شیء Post
    if instance.image:
        # بدست آوردن مسیر فایل تصویر
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
        if "default.jpg" not in image_path:
            # حذف فایل تصویر
            if os.path.exists(image_path):
                os.remove(image_path)