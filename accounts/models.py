from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user',default='default.jpg')

    def __str__(self) -> str:
        return self.username