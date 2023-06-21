from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
import os

class News(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.subject   


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    company = models.CharField(max_length=100)
    buylink = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='product')
    image2 = models.ImageField(upload_to='product')
    image3 = models.ImageField(upload_to='product')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-created_date',)

    def __str__(self) -> str:
        return self.title


@receiver(pre_delete, sender=Product)
def delete_product_images(sender, instance, **kwargs):
    # حذف تصویر مرتبط با شیء Post
    if instance.image1:
        # بدست آوردن مسیر فایل تصویر
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image1))
        # حذف فایل تصویر
        if os.path.exists(image_path):
            os.remove(image_path)
    if instance.image2:
        # بدست آوردن مسیر فایل تصویر
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image2))
        # حذف فایل تصویر
        if os.path.exists(image_path):
            os.remove(image_path)
    if instance.image3:
        # بدست آوردن مسیر فایل تصویر
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image3))
        # حذف فایل تصویر
        if os.path.exists(image_path):
            os.remove(image_path)


        